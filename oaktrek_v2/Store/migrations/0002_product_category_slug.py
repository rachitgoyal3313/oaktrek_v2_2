# Generated by Django 5.2 on 2025-04-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_slug',
            field=models.SlugField(blank=True),
        ),
    ]
