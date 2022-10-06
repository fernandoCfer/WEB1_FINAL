# Generated by Django 4.0.6 on 2022-09-24 16:06

import datetime
from django.db import migrations, models
import django.db.models.manager
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0004_imovel_favoritos_alter_imovel_data_imovel'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='imovel',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='imovel',
            name='data_imovel',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 24, 16, 6, 57, 394239, tzinfo=utc), verbose_name='data'),
        ),
    ]
