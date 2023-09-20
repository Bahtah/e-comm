# Generated by Django 4.2.5 on 2023-09-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField()),
            ],
        ),
    ]
