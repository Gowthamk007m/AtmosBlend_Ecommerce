# Generated by Django 4.1.7 on 2023-03-19 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_variant', '0011_alter_coupon_expiry_date'),
        ('cart', '0007_alter_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_variant.coupon'),
        ),
    ]