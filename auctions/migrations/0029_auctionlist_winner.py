# Generated by Django 3.1.1 on 2020-09-22 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0028_auctionlist_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlist',
            name='winner',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
