# Generated by Django 3.0 on 2020-05-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waev', '0002_auto_20200514_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='transcript',
            field=models.TextField(default=''),
        ),
    ]