# Generated by Django 3.2.5 on 2021-08-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_auto_20210802_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='글작성일'),
        ),
    ]
