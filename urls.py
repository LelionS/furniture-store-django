from django.urls import path
from .views import LandingPageView, CategoryDetailView
from django.conf import settings
from django.conf.urls.static import static
from .views import category_list

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/', category_list, name='category_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = [
    path('', category_list, name='category_list'),
]
