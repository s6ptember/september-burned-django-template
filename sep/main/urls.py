from django.urls import path
from .views import CatalogView, ItemDetailView

app_name = 'main'

urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),  
    path('item/<slug:slug>/', ItemDetailView.as_view(), name='item_detail'), 
]