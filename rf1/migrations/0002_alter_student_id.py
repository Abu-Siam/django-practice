# Generated by Django 4.0.6 on 2022-08-07 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rf1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
