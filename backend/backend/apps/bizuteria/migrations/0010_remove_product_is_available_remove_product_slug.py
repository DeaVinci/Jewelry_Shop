# Generated by Django 4.2.7 on 2024-06-08 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bizuteria', '0009_rename_uuid_f_order_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_available',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
