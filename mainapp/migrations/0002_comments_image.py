# Generated by Django 3.2.4 on 2021-08-12 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='commentS/'),
        ),
    ]
