# Generated by Django 2.2 on 2019-04-09 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='score',
            field=models.CharField(choices=[('GOOD', 'Good'), ('SO SO', 'So so'), ('BAD', 'Bad')], default='SO SO', max_length=2),
        ),
    ]