# Generated by Django 5.0.7 on 2025-06-07 08:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=10, null=True)),
                ('origin', models.CharField(max_length=100, null=True)),
                ('destination', models.CharField(max_length=100, null=True)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passengers', models.IntegerField(default=1)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('flight', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flight_app.flight')),
            ],
        ),
    ]
