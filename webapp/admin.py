from django.contrib import admin
from webapp.models import Article

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'created_at')
    list_filter = ('id', 'description', 'status', 'created_at')
    search_fields = ('description', 'status')
    fields = ('date', 'description', 'status', 'created_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Article, ArticleAdmin)
