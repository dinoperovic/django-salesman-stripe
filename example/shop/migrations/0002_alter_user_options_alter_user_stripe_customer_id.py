# Generated by Django 4.0.3 on 2022-03-21 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={},
        ),
        migrations.AlterField(
            model_name="user",
            name="stripe_customer_id",
            field=models.CharField(editable=False, max_length=128, null=True),
        ),
    ]
