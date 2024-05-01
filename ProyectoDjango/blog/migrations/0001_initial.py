# Generated by Django 5.0.2 on 2024-03-25 01:02

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('image', models.ImageField(default='null', upload_to='', verbose_name='Imagen')),
                ('public', models.BooleanField(verbose_name='¿Publicado?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
                ('update_at', models.DateTimeField(auto_now_add=True, verbose_name='Editado el')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('categories', models.ManyToManyField(blank=True, null=True, to='blog.category', verbose_name='categorias')),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
            },
        ),
    ]
