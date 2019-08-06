# Generated by Django 2.2.4 on 2019-08-06 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodasf', '0018_stf_link_journalist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nodasf.Venue'),
        ),
        migrations.AlterField(
            model_name='politician',
            name='upcoming',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodasf.Event'),
        ),
    ]