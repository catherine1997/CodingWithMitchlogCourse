# Generated by Django 3.2.4 on 2021-07-24 19:10

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=5000)),
                ('image', models.ImageField(upload_to=blog.models.upload_location)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_update', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
