# Generated by Django 3.1.1 on 2020-09-17 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20200917_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='auction',
            field=models.IntegerField(null=True),
        ),
    ]