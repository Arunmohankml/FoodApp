from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from .models import Sections
from .models import Items
from .models import ShopItems
from .models import Hotels
from .forms import HotelAddingForm
from .forms import ItemAddingForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def index(request):
    dict={'sections':Sections.objects.all(),
          'items':Items.objects.all(),
          }
    return render(request,'index.html', dict)

def loginPage(request):
    return render(request, 'login.html')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def itemsPage(request, section):
    current_section = get_object_or_404(Items, name=section)
    dict={'hotels':Hotels.objects.all(),
        'shopitems':ShopItems.objects.all(),
        'current_section': current_section,
    }
    return render(request, 'item.html', dict)

def register(request): 
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)  # Debug only

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def managePage(request):
    hotel = None
    items = None

    if request.user.role == 'owner':
        hotel = Hotels.objects.filter(owner=request.user.username).first()

    elif request.user.role == 'manager':
        hotel = Hotels.objects.filter(managers=request.user).first()

    if hotel:
        form = ItemAddingForm()
        items = ShopItems.objects.filter(hotel=hotel)
        types = Items.objects.filter(shopitems__in=items).distinct()
        return render(request, 'managePage.html', { 
            'form': form,
            'hotel': hotel,
            'types': types,
            'items': items,
        })

    
    form = HotelAddingForm()
    return render(request, 'managePage.html', {
        'form': form,
        'hotel': hotel,
    })
@login_required(login_url='login')
def add_restaurant(request):
    if request.method == "POST":
        form = HotelAddingForm(request.POST, request.FILES)
        if form.is_valid():
            hotel=form.save(commit=False)
            hotel.owner = request.user.username
            hotel.save()
            form.save_m2m()
            request.user.role="owner"
            request.user.save()
            return redirect('managePage')
    else:
        form = HotelAddingForm()
    
    return render(request, 'managePage.html', {'form': form})
    
@login_required(login_url='login')
def add_item(request):
    if request.method == "POST":
        form = ItemAddingForm(request.POST, request.FILES)
        if form.is_valid():
            hotel = None
            if request.user.role == 'owner':
                hotel = Hotels.objects.filter(owner=request.user.username).first()
            elif request.user.role == 'manager':
                hotel = Hotels.objects.filter(managers=request.user).first()
            
            shopItem=form.save(commit=False)
            shopItem.hotel=hotel
            shopItem.save()
            form.save_m2m()
            return redirect('managePage')
    else:
        form = ItemAddingForm()
    
    return render(request, 'managePage.html', {'form': form})

def edit_item(request, item_id):
    item = get_object_or_404(ShopItems, id=item_id)

    if request.method == 'POST':
        form = ItemAddingForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            shopItem=form.save(commit=False)
            shopItem.save()
            form.save_m2m()
            return redirect('managePage')  # Go back after save
    else:
        form = ItemAddingForm(instance=item)
    return redirect('managePage')  # Fallback


def search(request):
    query = request.GET.get('q', '')
    if query:
        hotels = Hotels.objects.filter(
            Q(name__icontains=query) |
            Q(bio__icontains=query) |
            Q(shop_items__name__icontains=query) |
            Q(shop_items__type__name__icontains=query)
        ).distinct()
    else:
        hotels = Hotels.objects.all()
    return render(request, 'searchPage.html', {'hotels': hotels})
