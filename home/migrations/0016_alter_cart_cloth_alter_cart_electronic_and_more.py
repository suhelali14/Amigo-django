# Generated by Django 4.2.4 on 2023-08-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cloth',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='electronic',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='grocery',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='sports',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cart',
            name='watches',
            field=models.IntegerField(),
        ),
    ]
