# Generated by Django 2.1.10 on 2019-07-30 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodasf', '0015_auto_20190730_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='politician',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='nodasf.County'),
        ),
    ]