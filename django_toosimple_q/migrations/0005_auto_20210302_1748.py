# Generated by Django 3.0.6 on 2021-03-02 16:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("toosimpleq", "0004_auto_20200507_1339"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="due",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="task",
            name="retries",
            field=models.IntegerField(
                default=0, help_text="retries left, -1 means infinite"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="retry_delay",
            field=models.IntegerField(
                default=0,
                help_text="Delay before next retry in seconds. Will double after each failure.",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="state",
            field=models.CharField(
                choices=[
                    ("QUEUED", "QUEUED"),
                    ("SLEEPING", "SLEEPING"),
                    ("PROCESSING", "PROCESSING"),
                    ("FAILED", "FAILED"),
                    ("SUCCEEDED", "SUCCEEDED"),
                    ("INVALID", "INVALID"),
                    ("INTERRUPTED", "INTERRUPTED"),
                ],
                default="QUEUED",
                max_length=32,
            ),
        ),
    ]
