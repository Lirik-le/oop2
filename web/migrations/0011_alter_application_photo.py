# Generated by Django 4.1.2 on 2022-11-14 12:31

import django.core.validators
from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_application_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='photo',
            field=models.ImageField(blank=True, max_length=254, null=True, upload_to='files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']), web.models.limited_image]),
        ),
    ]
