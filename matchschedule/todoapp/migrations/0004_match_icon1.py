# Generated by Django 3.2.2 on 2021-05-11 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_match_team2'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='icon1',
            field=models.ImageField(default='ddd', upload_to=''),
            preserve_default=False,
        ),
    ]