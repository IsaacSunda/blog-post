# Generated by Django 4.1 on 2023-02-10 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_remove_message_likes_message_like"),
    ]

    operations = [
        migrations.RenameField(
            model_name="message", old_name="like", new_name="likes",
        ),
    ]
