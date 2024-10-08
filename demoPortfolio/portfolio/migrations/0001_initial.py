# Generated by Django 5.0.6 on 2024-09-01 08:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Не больше 255 символов', max_length=255, verbose_name='Название проекта')),
                ('img_background', models.ImageField(upload_to='', verbose_name='Обложка проекта')),
                ('publication', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('date_changes', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TagName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Не больше 50 символов', max_length=50, verbose_name='Название категории')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('date_changes', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Существующая категория',
                'verbose_name_plural': 'Существующие категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('date_changes', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.project', verbose_name='Проект')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.tagname', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Проект и его категории',
                'verbose_name_plural': 'Проекты и их категории',
                'ordering': ['id'],
            },
        ),
    ]
