# Generated by Django 3.2.4 on 2021-09-25 12:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_alter_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likedUsers',
            field=models.ManyToManyField(blank=True, related_name='likedUsers', to=settings.AUTH_USER_MODEL),
        ),
    ]