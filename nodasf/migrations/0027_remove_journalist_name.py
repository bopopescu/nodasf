# Generated by Django 2.2.4 on 2019-12-03 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodasf', '0026_auto_20191203_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalist',
            name='name',
        ),
    ]