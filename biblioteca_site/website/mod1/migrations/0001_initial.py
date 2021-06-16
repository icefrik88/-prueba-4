# Generated by Django 3.2.4 on 2021-06-16 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('ISBN', models.IntegerField(primary_key=True, serialize=False, verbose_name='ISBN del libro')),
                ('nombreLibro', models.CharField(max_length=50, verbose_name='Nombre del libro')),
                ('autorLibro', models.CharField(max_length=60, verbose_name='Autor del libro')),
                ('descLibro', models.CharField(max_length=300, verbose_name='Descripcion del libro')),
                ('categoriaLibro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod1.categoria')),
            ],
        ),
    ]
