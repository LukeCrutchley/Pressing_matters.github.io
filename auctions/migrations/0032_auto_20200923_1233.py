# Generated by Django 3.1.1 on 2020-09-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0031_auto_20200923_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='auction_item',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
