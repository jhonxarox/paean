# Generated by Django 5.1.4 on 2024-12-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('img_path', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('genre', models.JSONField()),
                ('language', models.CharField(max_length=50)),
                ('mpaa_rating_type', models.CharField(max_length=10)),
                ('mpaa_rating_label', models.CharField(blank=True, max_length=255, null=True)),
                ('user_rating', models.IntegerField()),
            ],
        ),
    ]