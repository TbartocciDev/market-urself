# Generated by Django 4.2 on 2023-04-30 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_itemphoto_tablephoto_remove_item_categories_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user',
        ),
    ]