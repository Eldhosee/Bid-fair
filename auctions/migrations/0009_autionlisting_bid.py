# Generated by Django 4.0.4 on 2022-07-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_rename_wishlist_wishlists'),
    ]

    operations = [
        migrations.AddField(
            model_name='autionlisting',
            name='bid',
            field=models.BooleanField(default=0),
        ),
    ]
