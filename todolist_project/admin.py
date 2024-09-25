from django.contrib import admin

from todolist_project.models import Task, Tag

admin.site.register(Tag)
admin.site.register(Task)
