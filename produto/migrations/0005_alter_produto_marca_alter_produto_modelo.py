# Generated by Django 4.0.6 on 2022-09-19 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_remove_produto_nomdescricao_longa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='marca',
            field=models.CharField(default=' ', max_length=155),
        ),
        migrations.AlterField(
            model_name='produto',
            name='modelo',
            field=models.CharField(default=' ', max_length=155),
        ),
    ]
