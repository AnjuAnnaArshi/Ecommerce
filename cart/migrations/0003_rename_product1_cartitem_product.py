# Generated by Django 4.2 on 2023-05-12 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_product_cartitem_product1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product1',
            new_name='product',
        ),
    ]
