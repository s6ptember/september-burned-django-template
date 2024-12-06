from django.db import models


class Size(models.Model):
    ''' для добавления размерной сетки '''
    name = models.CharField(max_length=10, unique=True)  


    def __str__(self):
        return self.name



class Category(models.Model):
    ''' категории товаров '''
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name
    
    
    class Meta:
        ordering = ['name']
        indexes = [models.Index(fields=['name'])]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    
    def get_item_count(self):
        return Item.objects.filter(category=self).count()


class Item(models.Model):
    ''' модели самого товара '''
    name = models.CharField(max_length=255) 
    slug = models.SlugField(unique=True)  
    available = models.BooleanField(default=True) 
    sizes = models.ManyToManyField(Size, through='ItemSize', 
                                   related_name='items', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                 related_name='items', default=1)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0) 
    description = models.TextField(blank=True)


    def __str__(self):
        return self.name


    # высчитывает цену с учетом скидки
    def get_price_with_discount(self):
        if self.discount > 0:
            return self.price * (1 - (self.discount / 100))
        return self.price


class ItemSize(models.Model):
    ''' для добавления размеров в товаре '''
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)


    class Meta:
        unique_together = ('item', 'size')
        

class ItemImage(models.Model):
    ''' 
        для добавления фотографий, выводимых на 
        странице детальной информации
    '''
    product = models.ForeignKey(Item, related_name='images',
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    
    
    def __str__(self):
        return f'{self.product.name} - {self.image.name}'