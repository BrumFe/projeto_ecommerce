# Generated by Django 4.0.6 on 2022-09-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0008_alter_produto_descricao_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem_1',
            field=models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem_2',
            field=models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m/'),
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem_3',
            field=models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m/'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('V', 'Variável'), ('S', 'Simples')], default='V', max_length=1),
        ),
    ]
