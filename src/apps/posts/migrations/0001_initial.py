# Generated by Django 3.1.2 on 2020-11-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('name', models.TextField(verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('title', models.CharField(max_length=140, verbose_name='title')),
                ('slug_name', models.SlugField(max_length=140, unique=True)),
                ('content', models.TextField(blank=True, null=True, verbose_name='content')),
                ('excerpt', models.TextField(blank=True, null=True, verbose_name='excerpt')),
                ('picture', models.ImageField(blank=True, upload_to='posts/pictures')),
                ('status', models.CharField(choices=[('pu', 'Public'), ('pr', 'Private'), ('tr', 'Trash')], default='pr', max_length=2, verbose_name='status')),
            ],
            options={
                'ordering': ['-modified', '-created'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('name', models.TextField(verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
