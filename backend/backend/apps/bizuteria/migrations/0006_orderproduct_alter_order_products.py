# Generated by Django 4.2.7 on 2024-05-27 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bizuteria', '0005_rename_total_price_order_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bizuteria.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bizuteria.product')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
    ]