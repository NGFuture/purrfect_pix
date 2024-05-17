# Generated by Django 5.0.6 on 2024-05-16 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('temperament', models.CharField(max_length=255)),
                ('origin', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('life_span', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('breeds', models.ManyToManyField(to='users.breed')),
            ],
        ),
    ]