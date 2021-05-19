# Generated by Django 2.2.22 on 2021-05-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('subtitle', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('image', models.ImageField(default='default/static/news/images/default-news.jpeg', upload_to='uploads/images/')),
            ],
            options={
                'ordering': ['title'],
                'abstract': False,
            },
        ),
    ]
