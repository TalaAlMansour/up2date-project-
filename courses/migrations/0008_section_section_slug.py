# Generated by Django 5.0.3 on 2024-03-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_news_news_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='section_Slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
