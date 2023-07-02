from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=255, verbose_name='Ім\'я')
    email = models.EmailField(verbose_name='Email')
    content = models.TextField(verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')

    def __str__(self):
        return f' {self.content}'
    
    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['-created_at']