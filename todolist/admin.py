from django.contrib import admin
from todolist.models import Task


# Register your models here.
@admin.register(Task)
class TaskView(admin.ModelAdmin):
    list_display = ('manage', 'done', 'task')
    list_filter = ('manage',)


# admin.site.register(Task)