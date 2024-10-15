from django.views.generic import TemplateView, DetailView
from django.shortcuts import render
from .models import Category, Product, AlertMessage
from django.views.generic import DetailView
from .models import Category, Product
from django.views.generic import ListView
from .models import Product, Category, Subcategory

def landing_page(request):
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'store/landing_page.html', {'categories': categories})
class LandingPageView(TemplateView):
    template_name = 'store/landing_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  
        context['featured_products'] = Product.objects.all()[:6]
        context['alert_message'] = AlertMessage.objects.filter(is_active=True).first()  
        return context


class CategoryProductListView(ListView):
    model = Product
    template_name = 'store/category_products.html'   
    context_object_name = 'products'
    def get_queryset(self):
        category_slug = self.kwargs['slug']
        return Product.objects.filter(category__slug=category_slug)

class SubcategoryProductListView(ListView):
    model = Product
    template_name = 'store/subcategory_products.html'   
    context_object_name = 'products'
    def get_queryset(self):
        subcategory_slug = self.kwargs['slug']
        return Product.objects.filter(subcategory__slug=subcategory_slug)

class LandingPageView(TemplateView):
    template_name = 'store/landing_page.html'  

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'store/category_detail.html'  
    context_object_name = 'category'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.object.products.all()  
        return context

def landing_page_view(request):
    categories = Category.objects.all()
    return render(request, 'store/landing_page.html', {'categories': categories})

from django.shortcuts import render
from .models import Category, AlertMessage

def category_list(request):
    # Fetch all categories and prefetch related subcategories for optimization
    categories = Category.objects.prefetch_related('subcategories').all()
    
    # Fetch active alert messages if needed
    alerts = AlertMessage.objects.filter(is_active=True)

    context = {
        'categories': categories,
        'alerts': alerts,
    }

    return render(request, 'store/landing_page.html', context)


