# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greatideations', '0002_auto_20151106_2146'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ContactForm',
            new_name='ContactEntry',
        ),
        migrations.RenameField(
            model_name='contactentry',
            old_name='contact_message',
            new_name='message',
        ),
    ]
