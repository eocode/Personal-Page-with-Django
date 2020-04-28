from django.contrib import admin
from parler.admin import TranslatableAdmin

from portfolio.models import Project


class ProjectAdmin(TranslatableAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
admin.site.site_header = "EOCode Software"
