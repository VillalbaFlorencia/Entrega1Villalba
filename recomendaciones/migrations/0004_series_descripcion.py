# Generated by Django 4.0.3 on 2022-04-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomendaciones', '0003_rename_serie_documentales_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='descripcion',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
