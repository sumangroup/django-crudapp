# Generated by Django 4.2.3 on 2023-07-29 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_rename_admin_password_admin_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=256, verbose_name='Password'),
        ),
    ]
