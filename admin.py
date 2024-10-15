from django.contrib import admin
from .models import Category, Product, AlertMessage, Subcategory

class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'subcategory')
    list_filter = ('category', 'subcategory')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Subcategory)
admin.site.register(AlertMessage)
