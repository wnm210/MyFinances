# Generated by Django 5.0.3 on 2024-03-08 23:17

import django.db.models.deletion
from django.db import migrations, models

import backend.models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0022_loginlog_service_alter_verificationcodes_expiry_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="APIKey",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("service", models.CharField(choices=[("aws_api_destination", "Aws Api Destination")], max_length=20, null=True)),
                ("key", models.CharField(default=backend.core.models.RandomAPICode, max_length=100)),
                ("last_used", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "API Key",
                "verbose_name_plural": "API Keys",
            },
        ),
        migrations.CreateModel(
            name="InvoiceOnetimeSchedule",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("stored_schedule_arn", models.CharField(blank=True, max_length=100, null=True)),
                ("received", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("creating", "Creating"),
                            ("completed", "Completed"),
                            ("failed", "Failed"),
                            ("deleting", "Deleting"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="pending",
                        max_length=100,
                    ),
                ),
                ("due", models.DateTimeField()),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="onetime_invoice_schedules", to="backend.invoice"
                    ),
                ),
            ],
            options={
                "verbose_name": "One-Time Invoice Schedule",
                "verbose_name_plural": "One-Time Invoice Schedules",
            },
        ),
    ]
