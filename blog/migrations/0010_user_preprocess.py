# Generated by Django 3.1.14 on 2022-04-28 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20220331_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='preprocess',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='전저리 전 Codex 반환값'),
        ),
    ]
