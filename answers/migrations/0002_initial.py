
# Generated by Django 5.1.1 on 2024-10-02 14:56


import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('answers', '0001_initial'),
        ('screeningtestscore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='screeningtestscore.screeningtestscore'),
        ),
    ]
