# Generated by Django 2.2.14 on 2020-08-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
