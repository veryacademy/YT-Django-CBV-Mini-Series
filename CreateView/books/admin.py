from django.contrib import admin
from . import models


@admin.register(models.Books)
class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',), }
