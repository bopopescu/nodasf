# Generated by Django 2.2.4 on 2019-09-04 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodasf', '0022_politician_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='local_link',
            name='posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stf',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='stf_hub',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
