# Generated by Django 4.2.7 on 2024-05-30 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bizuteria', '0007_order_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='id',
            new_name='uuid_f',
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='bizuteria.order'),
        ),
    ]
