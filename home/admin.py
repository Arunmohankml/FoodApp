from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Sections
from .models import Items
from .models import ShopItems
from .models import Hotels

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Sections)
admin.site.register(Items)
admin.site.register(ShopItems)
admin.site.register(Hotels)