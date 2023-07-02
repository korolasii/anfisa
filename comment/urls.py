from django.urls import path
from .views import *

urlpatterns = [
    path('', comment_list, name='comment'),
    path('create_comment/', create, name='create_comment')
]