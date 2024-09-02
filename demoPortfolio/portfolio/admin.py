from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_a_img_background', 'publication',
                    'slug', 'date_creation', 'date_changes')
    list_display_links = ('id', 'name')
    search_fields = ('id',)
    list_editable = ('publication',)
    fields = ('name', ('img_background', 'get_html_img_background'),
              'publication', 'slug', 'date_creation', 'date_changes')
    readonly_fields = ('get_html_img_background', 'date_creation',
                       'date_changes')
    prepopulated_fields = {"slug": ("name",)}

    def get_html_a_img_background(self, object):
        if object.img_background:
            return mark_safe(f"<img src='{object.img_background.url}'"
                             f" width=50> <a href='{object.img_background.url}'"
                             f">{object.img_background}</a>")

    def get_html_img_background(self, object):
        if object.img_background:
            return mark_safe(
                f"<img src='{object.img_background.url}' width=50>")

    get_html_img_background.short_description = 'Изображение на данный момент'
    get_html_a_img_background.short_description = 'Обложка проекта'


class TagNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "slug", 'date_creation', 'date_changes')
    list_display_links = ('id', 'name')
    search_fields = ('id',)
    prepopulated_fields = {"slug": ("name",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'project', 'date_creation', 'date_changes')
    list_display_links = ('id',)
    search_fields = ('id',)
    list_filter = ('tag', 'project')


admin.site.register(Project, ProjectAdmin)
admin.site.register(TagName, TagNameAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.site_title = 'Админ-панель сайта Данила Селиния'
admin.site.site_header = 'Админ-панель сайта Данила Селиния'
