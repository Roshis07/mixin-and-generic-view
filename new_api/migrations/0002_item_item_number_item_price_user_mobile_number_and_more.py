# Generated by Django 4.2.4 on 2023-11-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_number',
            field=models.IntegerField(default=1111112),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=111111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='mobile_number',
            field=models.IntegerField(default=1111111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_number',
            field=models.IntegerField(default=111111),
            preserve_default=False,
        ),
    ]
