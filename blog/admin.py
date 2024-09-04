from django.contrib import admin
from blog.models import Post


# Register your models here.
admin.site.register(Post)

#@admin.register(Post)

# class PostAdmin(admin.ModelAdmin):
#      class Media:
#         js= ('tinyInject.js',)

# Tinymce plugins in myproject.venv>lib>django>contrib>admin>templates>admin>change_form_object_tools.html
