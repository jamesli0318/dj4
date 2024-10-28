from django.contrib import admin

# Register your models here.
from phone import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pmodel', 'nickname', 'price', 'year')
    search_fields = ('nickname',)
    ordering = ('-price',)
    
    
class MakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

    
class PModelAdmin(admin.ModelAdmin):
    list_display = ('maker', 'name', 'url')
    

class PPhotoAdmin(admin.ModelAdmin):
    list_display = ('product', 'url', 'media')

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Maker, MakerAdmin)
admin.site.register(models.PModel, PModelAdmin)
admin.site.register(models.PPhoto, PPhotoAdmin)
