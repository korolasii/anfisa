# Generated by Django 4.2.2 on 2023-06-30 12:08

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='category/', verbose_name='Зображення')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child', to='ice_cream.category')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='IceCream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Кількість')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Ціна')),
                ('on_main', models.BooleanField(default=True, verbose_name='На главную?')),
            ],
            options={
                'verbose_name': 'мороженое',
                'verbose_name_plural': 'мороженое',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основна')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ice_cream.category', verbose_name='Категорія')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ice_cream.icecream', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Категорія товару',
                'verbose_name_plural': 'Категорії товарів',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(null=True, upload_to='catalog/product/', verbose_name='Зображення')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основне')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ice_cream.icecream', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
        migrations.AddField(
            model_name='icecream',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='products', through='ice_cream.ProductCategory', to='ice_cream.category', verbose_name='Категорії'),
        ),
    ]
