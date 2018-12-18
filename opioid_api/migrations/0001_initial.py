# Generated by Django 2.1.4 on 2018-12-18 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opioids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.IntegerField()),
                ('location_name', models.CharField(max_length=1024)),
                ('sex_id', models.IntegerField()),
                ('sex_name', models.CharField(max_length=1024)),
                ('year', models.IntegerField()),
                ('val', models.DecimalField(decimal_places=20, max_digits=25)),
                ('upper', models.DecimalField(decimal_places=20, max_digits=25)),
                ('lower', models.DecimalField(decimal_places=20, max_digits=25)),
            ],
        ),
    ]
