from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin

from .models import Category, Post


class CategoryAdmin(TranslatableAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(TranslatableAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('translations__title', 'translations__content', 'categories__translations__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories')

    def post_categories(self, obj):
        return ", ".join(
            [c.name for c in obj.categories.all()])

    post_categories.short_description = _("Categorías")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
