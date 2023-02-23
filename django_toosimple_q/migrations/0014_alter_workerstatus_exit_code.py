# Generated by Django 4.1.4 on 2023-01-17 01:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("toosimpleq", "0013_workerstatus_exit_code_workerstatus_exit_log"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workerstatus",
            name="exit_code",
            field=models.IntegerField(
                blank=True,
                choices=[(0, "Stopped"), (77, "Terminated"), (99, "Crashed")],
                null=True,
            ),
        ),
    ]
