# Generated by Django 4.2.7 on 2024-05-28 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_city_user_house_number_user_phone_user_street_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='zip_code',
            new_name='zipCode',
        ),
    ]