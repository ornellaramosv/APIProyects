from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    readonly_fields = ('highlighted',)


admin.site.register(Snippet, SnippetAdmin)
