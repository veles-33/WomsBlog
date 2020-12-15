from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    """Категория"""

    title = models.CharField(verbose_name="Название", max_length=50)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        
    def __str__(self):
        return self.title
    
    
class Tag(models.Model):
    """Тег"""
    
    title = models.CharField(verbose_name="Тег", max_length=50)
    
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        
    def __str__(self):
        return self.title
    
    
class News(models.Model):
    """Новость"""
    
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    title = models.CharField(verbose_name="Заголовок", max_length=100)
    text_min = models.TextField(verbose_name="Мин. текст", max_length=350)
    text = models.TextField(verbose_name="Текст статьи")
    tags = models.ManyToManyField(Tag, verbose_name="Теги")
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    description = models.CharField(verbose_name="Описание", max_length=100)
    keywords = models.CharField(verbose_name="Ключевые слова", max_length=50)
    
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        
    def __str__(self):
        return self.title
