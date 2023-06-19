from django.urls import path
from .views import *

# Эта строчка обязательна. 
# Без нее чуда не произойдет и namespace работать не будет
app_name = 'ice_cream'

urlpatterns = [
    # Главная страница
    path('', index, name='index'),
    # Список мороженого
    path('ice_cream/', ice_cream_list, name='ice_cream_list'),
    # Подробная информация о мороженом. Ждем пременную типа int, 
    # и будем использовать ее под именем pk
    path('ice_cream/<int:pk>/', ice_cream_detail, name='ice_cream_detail'),
]