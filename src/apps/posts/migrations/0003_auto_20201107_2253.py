# Generated by Django 3.1.2 on 2020-11-07 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20201107_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('PU', 'Public'), ('PR', 'Private'), ('TR', 'Trash')], default='PR', max_length=2, verbose_name='status'),
        ),
    ]
