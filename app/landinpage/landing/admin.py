from django.contrib import admin

# Register your models here.
from .models import *


class HomePageAdmin(admin.ModelAdmin):
    list_display = ('id','key', 'value')
    list_display_links = ('id','key', "value")
    search_fields = ('key', "value")

class MenuAdmin(admin.ModelAdmin):
    list_display = ('id','key', 'value', 'link')
    list_display_links = ('id','key', "value", 'link')
    search_fields = ('key', "value", 'link')

class AboutUSModelAdmin(admin.ModelAdmin):
    list_display = ('id','key', 'value')
    list_display_links = ('id','key', "value")
    search_fields = ('key', "value")

class ContactSModelAdmin(admin.ModelAdmin):
    list_display = ('id','key', 'value')
    list_display_links = ('id','key', "value")
    search_fields = ('key', "value")

admin.site.register(ContactSModel, ContactSModelAdmin)
admin.site.register(AboutUSModel, AboutUSModelAdmin )
admin.site.register(Menu, MenuAdmin)
admin.site.register(HomePage, HomePageAdmin)