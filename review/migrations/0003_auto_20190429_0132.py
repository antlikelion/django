# Generated by Django 2.2 on 2019-04-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20190410_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publisher',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='writer',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='score',
            field=models.CharField(choices=[('☆☆☆☆☆', '☆☆☆☆☆'), ('☆☆☆☆', '☆☆☆☆'), ('☆☆☆', '☆☆☆'), ('☆☆', '☆☆'), ('☆', '☆')], max_length=5),
        ),
    ]
