# Generated by Django 2.2.6 on 2019-12-18 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Laboratory', '0002_report_analysis_analyst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_analysis',
            name='analyst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Laboratory.Laboratorist'),
        ),
    ]
