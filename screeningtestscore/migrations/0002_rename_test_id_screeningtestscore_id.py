# Generated by Django 5.1.1 on 2024-09-25 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('screeningtestscore', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screeningtestscore',
            old_name='test_id',
            new_name='id',
        ),
    ]
