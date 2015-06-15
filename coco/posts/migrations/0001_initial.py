# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('hits', models.IntegerField(null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('user_id', models.ForeignKey(to='users.BaseUser')),
            ],
            options={
                'verbose_name': '\uac8c\uc2dc\uae00',
            },
        ),
    ]
