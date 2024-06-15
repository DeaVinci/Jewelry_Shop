# Generated by Django 4.2.7 on 2024-06-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bizuteria', '0011_alter_product_fineness_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fineness',
            field=models.CharField(blank=True, default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='long_description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='metal',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
