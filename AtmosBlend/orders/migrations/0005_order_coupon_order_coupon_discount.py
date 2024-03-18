# Generated by Django 4.1.7 on 2023-03-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='coupon_discount',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
