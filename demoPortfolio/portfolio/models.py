from functools import cached_property

from django.db import models
from django.urls import reverse
from cms.models.fields import PlaceholderRelationField
from cms.utils.placeholder import get_placeholder_from_slot


class Project(models.Model):
    name = models.CharField(max_length=255, help_text='Не больше 255 символов',
                            verbose_name='Название проекта')
    img_background = models.ImageField(verbose_name='Обложка проекта')
    publication = models.BooleanField(default=False,
                                      verbose_name='Опубликовано')
    date_creation = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True,
                                        verbose_name='Время изменения')
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL")

    placeholder = PlaceholderRelationField()

    @cached_property
    def content(self):
        return get_placeholder_from_slot(self.placeholder, "content")


    def get_template(self):
        """
            Need for edit placeholder in apphook
        """
        return "app_portfolio/project_page.html"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:project_page', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['id']


class TagName(models.Model):
    name = models.CharField(max_length=50, help_text='Не больше 50 символов',
                            verbose_name='Название категории')
    date_creation = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True,
                                        verbose_name='Время изменения')
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio:tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Существующая категория'
        verbose_name_plural = 'Существующие категории'
        ordering = ['id']


class Tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                verbose_name='Проект')
    tag = models.ForeignKey(TagName, on_delete=models.CASCADE,
                            verbose_name='Категория')
    date_creation = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Время создания')
    date_changes = models.DateTimeField(auto_now=True,
                                        verbose_name='Время изменения')

    class Meta:
        verbose_name = 'Проект и его категории'
        verbose_name_plural = 'Проекты и их категории'
        ordering = ['id']