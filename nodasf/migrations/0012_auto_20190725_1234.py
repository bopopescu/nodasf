# Generated by Django 2.1.10 on 2019-07-25 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodasf', '0011_auto_20190725_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='nodasf.County'),
        ),
    ]
