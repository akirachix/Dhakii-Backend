# Generated by Django 5.1.2 on 2024-10-30 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('nurse_id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('reg_no', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sub_location', models.CharField(max_length=255)),
                ('village', models.CharField(default='Village', max_length=255)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.hospital')),
            ],
        ),
    ]
