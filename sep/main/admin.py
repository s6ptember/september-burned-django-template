from django.contrib import admin
from .models import Size, Category, Item, \
    ItemSize, ItemImage


class ItemSizeInline(admin.TabularInline):
    model = ItemSize
    extra = 1  
    

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 5


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 
                    'available', 'price', 'discount', 
                    'created_at', 'updated_at')
    list_filter = ('available', 'category')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-created_at',)
    inlines = [ItemSizeInline, ItemImageInline] 
