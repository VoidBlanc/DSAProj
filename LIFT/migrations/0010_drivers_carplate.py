# Generated by Django 4.0.3 on 2022-03-28 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LIFT', '0009_rename_data_pathcache_graph_pathcache_heuristic'),
    ]

    operations = [
        migrations.AddField(
            model_name='drivers',
            name='carplate',
            field=models.TextField(default=''),
        ),
    ]
