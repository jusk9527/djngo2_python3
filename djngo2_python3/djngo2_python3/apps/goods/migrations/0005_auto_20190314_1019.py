# Generated by Django 2.0.2 on 2019-03-14 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20190314_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='category',
            new_name='category_name',
        ),
    ]