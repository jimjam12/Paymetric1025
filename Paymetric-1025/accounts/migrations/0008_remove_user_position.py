# Generated by Django 4.1.1 on 2022-10-13 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_user_department_user_accounting_user_hr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
    ]