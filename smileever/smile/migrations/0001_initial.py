# Generated by Django 3.1.1 on 2020-10-12 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('treatment', models.TextField()),
                ('msg', models.TextField()),
            ],
        ),
    ]