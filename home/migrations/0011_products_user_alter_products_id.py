# Generated by Django 4.2.4 on 2023-08-15 05:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='user',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
