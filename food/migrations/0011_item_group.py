# Generated by Django 5.1.7 on 2025-03-27 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0010_item_user_name'),
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='group',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='group.group'),
        ),
    ]
