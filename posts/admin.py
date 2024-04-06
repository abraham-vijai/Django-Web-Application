from django.contrib import admin
from .models import Photo, Post

# Register your models here.

admin.site.register(Post)
admin.site.register(Photo)