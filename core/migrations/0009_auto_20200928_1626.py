# Generated by Django 2.2.14 on 2020-09-28 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200928_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AlterField(
            model_name='itemimages',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Item'),
        ),
    ]
