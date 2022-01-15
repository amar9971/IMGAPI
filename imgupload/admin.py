from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile


# Register your models here.
class profileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','picture']


admin.site.register(Profile, profileAdmin)
