# Generated by Django 3.2.3 on 2021-05-22 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
