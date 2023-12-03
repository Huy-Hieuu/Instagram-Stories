# Generated by Django 4.2.5 on 2023-09-29 12:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stories", "0002_alter_userstory_media_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userstory",
            name="expired",
        ),
        migrations.AddField(
            model_name="userstory",
            name="status",
            field=models.CharField(
                choices=[("NEW", "New"), ("EXPIRED", "Expired")],
                default="NEW",
                max_length=50,
            ),
        ),
    ]