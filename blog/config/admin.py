from django.contrib import admin
from .models import Blog, Author, Entry, Topic

admin.site.register(Topic)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)