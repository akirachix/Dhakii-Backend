# Generated by Django 5.1.2 on 2024-10-30 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community_health_promoter', '0001_initial'),
        ('mother', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScreeningTestScore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('test_date', models.DateField()),
                ('total_score', models.PositiveSmallIntegerField()),
                ('chp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community_health_promoter.chp')),
                ('mother_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mother.mother')),
            ],
        ),
    ]
