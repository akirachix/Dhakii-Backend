# Generated by Django 5.1.1 on 2024-10-26 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.CharField(blank=True, choices=[('nurse_admin', 'NurseAdmin'), ('nurse', 'Nurse'), ('chp', 'Community Health Promoter')], max_length=50, null=True),
        ),
    ]
