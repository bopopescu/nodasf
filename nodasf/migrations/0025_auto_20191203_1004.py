# Generated by Django 2.2.4 on 2019-12-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodasf', '0024_auto_20191010_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journalist',
            options={'ordering': ('last_name',)},
        ),
        migrations.RenameField(
            model_name='journalist',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='journalist',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]