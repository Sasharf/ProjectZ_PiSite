# Generated by Django 2.0 on 2017-12-28 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20171227_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorslogs',
            name='pi_mac',
            field=models.CharField(default='00:00:00:00:00:00', max_length=250),
        ),
    ]