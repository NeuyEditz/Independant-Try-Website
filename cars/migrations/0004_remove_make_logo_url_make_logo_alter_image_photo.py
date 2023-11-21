# Generated by Django 4.2.5 on 2023-11-12 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_remove_image_url_image_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='make',
            name='logo_url',
        ),
        migrations.AddField(
            model_name='make',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
