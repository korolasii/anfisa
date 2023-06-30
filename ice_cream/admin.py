from django.contrib import admin

from .models import *


    
    
class IceCreamInline(admin.TabularInline):
    model = IceCream.category.through
    extra = 1
    
class ImageInline(admin.TabularInline):
    model = Image
    fields = ('product', 'image_tag', 'image', 'is_main')
    readonly_fields = ('image_tag',)
    extra = 1


admin.site.register(Image)




@admin.register(IceCream)
class IceCreaProductAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'quantity', 'price')
    inlines = (IceCreamInline, ImageInline)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = ('name', 'image_tag_thumbnail')
    prepopulated_fields = {'slug': ('name',)}
    
    readonly_fields = ('image_tag_thumbnail',)
