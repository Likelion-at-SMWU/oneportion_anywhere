# Generated by Django 3.2.6 on 2021-08-11 22:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0012_merge_0009_auto_20210807_2112_0011_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='top_fixed',
            field=models.BooleanField(default=False, verbose_name='상단고정'),
        ),
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(default='관리자', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='community', to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
