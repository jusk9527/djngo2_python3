# Generated by Django 2.0.2 on 2019-03-14 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_goods_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='category_name',
            new_name='category',
        ),
    ]
