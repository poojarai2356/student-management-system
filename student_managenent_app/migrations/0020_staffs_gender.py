# Generated by Django 3.2.13 on 2022-05-03 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0019_staffs_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='gender',
            field=models.CharField(default='Male', max_length=50),
        ),
    ]
