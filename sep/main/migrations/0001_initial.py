# Generated by Django 5.1.4 on 2024-12-06 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='main_catego_name_5111b9_idx')],
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('available', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.size')),
            ],
            options={
                'unique_together': {('item', 'size')},
            },
        ),
        migrations.AddField(
            model_name='item',
            name='sizes',
            field=models.ManyToManyField(blank=True, related_name='items', through='main.ItemSize', to='main.size'),
        ),
    ]