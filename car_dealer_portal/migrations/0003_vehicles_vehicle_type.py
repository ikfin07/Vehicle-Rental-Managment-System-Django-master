# Generated by Django 2.2.7 on 2019-11-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealer_portal', '0002_cardealer_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='Vehicle_Type',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]