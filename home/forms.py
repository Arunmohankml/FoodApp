from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Hotels
from .models import ShopItems
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        cleaned_username = username.replace(' ', '_')

        # Check if the modified username already exists
        if CustomUser.objects.filter(username=cleaned_username).exists():
            raise forms.ValidationError("This username (after formatting) is already taken.")

        return cleaned_username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["username"]  # already cleaned above
        if commit:
            user.save()
        return user
    
    
class HotelAddingForm(forms.ModelForm):
    class Meta:
        model = Hotels
        fields = ['name', 'location', 'image', 'bio', 'rating', 'time', 'email', 'number1', 'number2']
        widgets = {
            'time': forms.Textarea(attrs={
                'placeholder': 'Enter JSON like {"mon": "9AM-5PM", "tue": "10AM-4PM"}',
                'rows': 3
            }),
        }

class ItemAddingForm(forms.ModelForm):
    class Meta:
        model = ShopItems
        fields = ['name', 'image', 'desc', 'section', 'type']