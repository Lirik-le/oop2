# Generated by Django 4.1.2 on 2022-11-22 11:27

import django.core.validators
from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_alter_application_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='comment',
            field=models.TextField(blank=True, max_length=500, verbose_name='Комментарий'),
        ),
        migrations.AddField(
            model_name='application',
            name='design',
            field=models.ImageField(blank=True, help_text='Максимальный размер изображения 2MB', null=True, upload_to=web.models.get_name_file, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'bmp']), web.models.limited_image], verbose_name='Картинка'),
        ),
    ]
