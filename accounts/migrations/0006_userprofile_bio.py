# Generated by Django 5.0.3 on 2024-03-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_user_imag_userprofile_user_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, default='Hey there, I am a blogicraft User', max_length=100),
        ),
    ]
