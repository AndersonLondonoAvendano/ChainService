from django.contrib import admin
from .models import posts
# Register your models here.

class postsAdmin(admin.ModelAdmin):
    readonly_fields= ("created",)
admin.site.register(posts, postsAdmin)