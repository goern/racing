# Generated by Django 4.2.8 on 2023-12-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("b4mad_racing_website", "0004_profile_driver_alter_copilotinstance_copilot"),
    ]

    operations = [
        migrations.AddField(
            model_name="copilot",
            name="long_description",
            field=models.TextField(default=""),
        ),
    ]
