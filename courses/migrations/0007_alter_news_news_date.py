# Generated by Django 5.0.3 on 2024-03-19 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_news_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
