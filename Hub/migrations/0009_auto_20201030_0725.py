# Generated by Django 3.1.1 on 2020-10-30 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0008_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='Date',
            field=models.DateTimeField(null=True),
        ),
    ]