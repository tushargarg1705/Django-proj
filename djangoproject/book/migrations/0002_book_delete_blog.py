# Generated by Django 4.1.7 on 2023-03-07 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=150)),
                ('Price', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
