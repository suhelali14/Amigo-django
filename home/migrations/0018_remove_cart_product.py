# Generated by Django 4.2.4 on 2023-08-15 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
    ]
