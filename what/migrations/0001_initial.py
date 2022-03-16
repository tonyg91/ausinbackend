# Generated by Django 4.0.3 on 2022-03-16 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100)),
                ('deal', models.CharField(max_length=300)),
                ('previousprice', models.IntegerField(verbose_name=8)),
                ('duration', models.DateTimeField(verbose_name=100)),
            ],
        ),
        migrations.CreateModel(
            name='Past',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pastevent', models.CharField(max_length=100)),
                ('pastdescription', models.CharField(max_length=300)),
                ('pastdate', models.DateField(max_length=8)),
                ('pastlocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=200)),
                ('history', models.CharField(max_length=300)),
                ('whattosee', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='What',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('date', models.DateField(max_length=8)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
