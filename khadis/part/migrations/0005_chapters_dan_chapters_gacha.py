# Generated by Django 4.2.6 on 2023-11-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0004_rename_khadises_t_khadises'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapters',
            name='dan',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='chapters',
            name='gacha',
            field=models.IntegerField(default=1),
        ),
    ]
