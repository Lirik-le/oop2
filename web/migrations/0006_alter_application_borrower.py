# Generated by Django 4.1.2 on 2022-11-06 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_application_borrower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='borrower',
            field=models.ForeignKey(blank=True, default='User', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]