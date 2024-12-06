from django.views.generic import ListView, DetailView
from .models import Item, Category, Size, ItemSize
from django.db.models import Q


class CatalogView(ListView):
    '''
        главное представление каталога
        
        методы сортировки товаров - по категории, по размеру, по интервалу цены
        
    '''
    model = Item
    # указываем расположение шаблона
    template_name = 'main/product/catalog.html'
    context_object_name = 'items'
    
    
    # собираем сортировки
    def get_queryset(self):
        queryset = super().get_queryset()
        category_slugs = self.request.GET.getlist('category')
        size_names = self.request.GET.getlist('size')
        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if category_slugs:
            queryset = queryset.filter(category__slug__in=category_slugs)

        if size_names:
            queryset = queryset.filter(
                Q(sizes__name__in=size_names) & Q(sizes__itemsize__available=True)
            ).distinct()

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


    # передаем контекст
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['sizes'] = Size.objects.all()
        context['selected_categories'] = self.request.GET.getlist('category') 
        context['selected_sizes'] = self.request.GET.getlist('size') 
        context['min_price'] = self.request.GET.get('min_price', '')
        context['max_price'] = self.request.GET.get('max_price', '')
        return context
    

# страница товара
class ItemDetailView(DetailView):
    model = Item
    template_name = 'main/product/detail.html'
    context_object_name = 'item'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.object
        available_sizes = ItemSize.objects.filter(item=item, available=True) 
        context['available_sizes'] = available_sizes
        return context
    