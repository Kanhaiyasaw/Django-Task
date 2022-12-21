# Generated by Django 4.1.4 on 2022-12-21 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='basic_field',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('is_basic_class', models.BooleanField()),
                ('email', models.EmailField(max_length=200)),
                ('address', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='duble_ex_field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeof_dispatch', models.TimeField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ex_field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Date_purchase', models.DateTimeField()),
                ('product', models.ImageField(upload_to='')),
            ],
        ),
    ]
