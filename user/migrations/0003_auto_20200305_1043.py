# Generated by Django 3.0 on 2020-03-05 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200305_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
    ]