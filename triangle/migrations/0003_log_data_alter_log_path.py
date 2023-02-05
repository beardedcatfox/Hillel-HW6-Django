# Generated by Django 4.1.5 on 2023-02-05 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('triangle', '0002_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='data',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='log',
            name='path',
            field=models.CharField(max_length=255),
        ),
    ]
