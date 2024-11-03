# Generated by Django 5.1.2 on 2024-10-30 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community_health_promoter', '0001_initial'),
        ('hospital', '0001_initial'),
        ('next_of_kin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mother',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('no_of_children', models.PositiveIntegerField()),
                ('registered_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tel_no', models.CharField(max_length=15)),
                ('marital_status', models.CharField(max_length=20)),
                ('sub_location', models.CharField(max_length=255)),
                ('village', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(1, 'Due Visit'), (0, 'Visited'), (-1, 'Missed Visit')], default=1, help_text='1: Due Visit, 0: Visited, -1: Missed Visit')),
                ('chp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='community_health_promoter.chp')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
                ('kin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='next_of_kin.nextofkin')),
            ],
        ),
    ]
