# Generated by Django 4.1.1 on 2022-09-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='employee',
            field=models.BooleanField(default=False),
        ),
    ]
