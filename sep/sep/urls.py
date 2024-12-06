from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # логин, регистрация, выход с профиля
    path('users/', include('users.urls', namespace='users')),
    # каталог, страница продукта
    path('', include('main.urls', namespace='main')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)