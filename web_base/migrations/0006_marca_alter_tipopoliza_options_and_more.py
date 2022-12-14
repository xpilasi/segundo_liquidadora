# Generated by Django 4.0.5 on 2022-09-12 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_base', '0005_tipopoliza_tiposiniestro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_marca', models.CharField(max_length=100, verbose_name='Código marca')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca')),
                ('creado_el', models.DateTimeField(auto_now_add=True, verbose_name='Creado el')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'ordering': ['-creado_el'],
            },
        ),
        migrations.AlterModelOptions(
            name='tipopoliza',
            options={'ordering': ['-creado_el'], 'verbose_name': 'Tipo de póliza', 'verbose_name_plural': 'Tipos de póliza'},
        ),
        migrations.AlterModelOptions(
            name='tiposiniestro',
            options={'ordering': ['-creado_el'], 'verbose_name': 'Tipo Siniestro', 'verbose_name_plural': 'Tipos de siniestro'},
        ),
        migrations.AlterModelOptions(
            name='tipovehiculo',
            options={'ordering': ['-creado_el'], 'verbose_name': 'Tipo de vehículo', 'verbose_name_plural': 'Tipos de vehículos'},
        ),
    ]
