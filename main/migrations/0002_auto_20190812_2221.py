# Generated by Django 2.2.3 on 2019-08-12 22:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 12, 22, 21, 23, 310319), verbose_name='date published'),
        ),
    ]
