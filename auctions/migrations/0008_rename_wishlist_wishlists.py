# Generated by Django 4.0.4 on 2022-07-07 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_wishlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='wishlist',
            new_name='wishlists',
        ),
    ]
