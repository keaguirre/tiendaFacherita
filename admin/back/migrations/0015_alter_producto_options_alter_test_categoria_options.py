# Generated by Django 4.1.4 on 2023-02-25 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0014_rename_admin_administrador'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ['categoria'], 'verbose_name': 'Producto old', 'verbose_name_plural': 'Producto old'},
        ),
        migrations.AlterModelOptions(
            name='test_categoria',
            options={'ordering': ['cat_id'], 'verbose_name': 'Test_Categoria', 'verbose_name_plural': 'Test_Categoria'},
        ),
    ]