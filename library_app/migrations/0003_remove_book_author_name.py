# Generated by Django 4.2.9 on 2024-05-23 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_book_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author_name',
        ),
    ]
