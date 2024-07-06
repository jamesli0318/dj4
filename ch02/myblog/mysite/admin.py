from django.contrib import admin
from mysite.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'pub_date')
# Register your models here.
admin.site.register(Post, PostAdmin)