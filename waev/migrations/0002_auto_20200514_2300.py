# Generated by Django 3.0 on 2020-05-14 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waev', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='transcript',
            field=models.TextField(null=True),
        ),
    ]
