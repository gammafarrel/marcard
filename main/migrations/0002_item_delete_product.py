# Generated by Django 4.2.4 on 2023-09-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('power', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]