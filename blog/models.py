from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    tresh = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Содержимое')
    image = models.ImageField(upload_to='photos/', verbose_name='Избражение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publication_sign = models.BooleanField(default=True, verbose_name='Признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Количество публикации')

    def __str__(self):
        return f'{self.title} Дата публикации:{self.created_at} Количество просмотров:{self.views_count}'
