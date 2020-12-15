from django.contrib import admin

from news.models import News
from news.models import Category
from news.models import Tag


admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)
