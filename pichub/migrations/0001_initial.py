# Generated by Django 3.1.3 on 2020-11-14 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('photo_description', models.TextField()),
                ('photo', models.ImageField(default='image.jpg', upload_to='images/')),
            ],
        ),
    ]