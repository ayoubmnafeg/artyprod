from django.contrib import admin
from .models import Client, Service, Project, Project_tag, Staff

# Register your models here.
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Project_tag)
admin.site.register(Staff)