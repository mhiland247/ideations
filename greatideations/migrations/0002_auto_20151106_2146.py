# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greatideations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='message',
            new_name='contact_message',
        ),
    ]
