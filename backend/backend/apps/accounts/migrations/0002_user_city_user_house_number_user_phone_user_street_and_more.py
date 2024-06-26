# Generated by Django 4.2.7 on 2024-05-11 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='Opole', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='house_number',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='123123123', max_length=15),
        ),
        migrations.AddField(
            model_name='user',
            name='street',
            field=models.CharField(default='Opole', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.CharField(default='42-323', max_length=10),
        ),
    ]
