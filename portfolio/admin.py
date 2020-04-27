from django.contrib import admin

from portfolio.models import Project


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Project, ProjectAdmin)
admin.site.site_header = "EOCode Software"
