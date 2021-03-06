# Generated by Django 3.1.1 on 2020-09-15 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_auto_20200915_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='auction',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='key', to='auctions.auctionlist'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
