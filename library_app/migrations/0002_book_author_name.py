# Generated by Django 4.2.9 on 2024-05-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]