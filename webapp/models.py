from django.db import models

# Create your models here.


class Article(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False, verbose_name="Описание")
    status = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Статус")
    date = models.CharField(max_length=200, null=False, blank=False, verbose_name="Дата")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время и дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время и дата обновления")

    def __str__(self):
        return f"{self.description} - {self.date}"
