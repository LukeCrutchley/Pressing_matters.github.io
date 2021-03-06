# Generated by Django 3.1.1 on 2020-09-11 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20200909_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlist',
            name='catagory',
            field=models.CharField(choices=[('other', 'Other'), ('fashion', 'Fashion'), ('toys', 'Toys'), ('electronics', 'Electronics'), ('home', 'Home')], default='Other', max_length=100),
        ),
        migrations.AlterField(
            model_name='auctionlist',
            name='description',
            field=models.CharField(default='Enter description here.', max_length=100),
        ),
        migrations.AlterField(
            model_name='auctionlist',
            name='image',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]
