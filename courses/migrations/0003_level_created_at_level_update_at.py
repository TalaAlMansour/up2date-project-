# Generated by Django 5.0.3 on 2024-03-12 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_level_video_level_leveltitle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='level',
            name='update_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]