# Generated by Django 3.1.4 on 2021-01-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shift_rota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('application', models.CharField(max_length=50, null=True)),
                ('Resource_Analyst', models.CharField(max_length=50, null=True)),
                ('shift_date', models.DateField()),
                ('shift', models.CharField(max_length=4)),
            ],
        ),
    ]
