# Generated by Django 4.2.7 on 2024-05-30 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bizuteria', '0008_rename_id_order_uuid_f_alter_orderproduct_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='uuid_f',
            new_name='id',
        ),
    ]
