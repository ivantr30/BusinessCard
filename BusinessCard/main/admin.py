from django.contrib import admin

from main.models import ApplicationModel
from main.models import ProjectModel

# Register your models here.
admin.site.register(ApplicationModel)
admin.site.register(ProjectModel)