# Generated by Django 4.1.5 on 2023-01-14 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_post_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ststus',
            field=models.CharField(choices=[('active', 'Active'), ('draft', 'Draft')], default='active', max_length=10),
        ),
    ]
