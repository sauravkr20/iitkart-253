# Generated by Django 4.0.3 on 2022-03-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customer_sell_seller_alter_sell_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]
