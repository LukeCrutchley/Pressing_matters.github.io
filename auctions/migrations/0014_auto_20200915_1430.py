# Generated by Django 3.1.1 on 2020-09-15 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
