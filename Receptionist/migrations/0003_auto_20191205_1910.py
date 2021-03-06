# Generated by Django 2.2.6 on 2019-12-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receptionist', '0002_receptionist_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254)),
                ('cnic', models.CharField(max_length=13)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('UnFit', 'Unfit'), ('Fit', 'Fit')], default='Pending', max_length=13)),
            ],
        ),
        migrations.AlterField(
            model_name='receptionist',
            name='status',
            field=models.IntegerField(choices=[(2, 2), (1, 1), (3, 3)], default=1),
        ),
    ]
