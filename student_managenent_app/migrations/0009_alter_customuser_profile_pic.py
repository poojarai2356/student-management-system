# Generated by Django 3.2.13 on 2022-04-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0008_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='avatar.svg', null=True, upload_to='profile_pic'),
        ),
    ]
