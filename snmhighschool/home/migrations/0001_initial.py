# Generated by Django 4.2.2 on 2023-06-19 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_no', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=50)),
                ('gname', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
