# Generated by Django 3.2.5 on 2022-03-24 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("toosimpleq", "0015_scheduleexec_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scheduleexec",
            name="state",
            field=models.CharField(
                choices=[("ACTIVE", "Active"), ("INVALID", "Invalid")],
                default="ACTIVE",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="taskexec",
            name="state",
            field=models.CharField(
                choices=[
                    ("QUEUED", "Queued"),
                    ("SLEEPING", "Sleeping"),
                    ("PROCESSING", "Processing"),
                    ("FAILED", "Failed"),
                    ("SUCCEEDED", "Succeeded"),
                    ("INVALID", "Invalid"),
                    ("INTERRUPTED", "Interrupted"),
                ],
                default="QUEUED",
                max_length=32,
            ),
        ),
    ]
