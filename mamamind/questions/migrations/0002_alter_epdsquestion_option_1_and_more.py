# Generated by Django 5.1.1 on 2024-09-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='epdsquestion',
            name='option_1',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='epdsquestion',
            name='option_2',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='epdsquestion',
            name='option_3',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='epdsquestion',
            name='option_4',
            field=models.TextField(),
        ),
    ]
