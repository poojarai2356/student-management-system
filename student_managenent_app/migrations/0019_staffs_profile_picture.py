# Generated by Django 3.2.13 on 2022-05-03 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0018_alter_students_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='profile_picture',
            field=models.ImageField(blank=True, default='avatar.svg', null=True, upload_to='staffs_profile_pic'),
        ),
    ]
