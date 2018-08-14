from django.contrib import admin
#imports from app
from url_app import models

# Register your models here.
class URLAdmin(admin.ModelAdmin):
    list_display = ['id', 'url', 'shortcode','updated','timestamp']
    ordering = ['id']

admin.site.register(models.Url,URLAdmin)
