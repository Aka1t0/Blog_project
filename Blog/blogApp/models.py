from django.db import models
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Именование')
    email = models.EmailField(blank=True, verbose_name='Голубиная почта')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Творец')
    body = models.TextField(verbose_name='Наполнение')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])