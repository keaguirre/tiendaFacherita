# Generated by Django 4.1.4 on 2023-02-25 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0015_alter_producto_options_alter_test_categoria_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria1',
            options={'ordering': ['cat_id'], 'verbose_name': 'Categoria1', 'verbose_name_plural': 'Categorias1'},
        ),
        migrations.AlterModelOptions(
            name='producto1',
            options={'ordering': ['prod_id'], 'verbose_name': 'Producto1', 'verbose_name_plural': 'Productos1'},
        ),
    ]
