# Generated by Django 3.1.14 on 2022-02-02 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userid', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='사용자 아이디')),
                ('username', models.CharField(max_length=50, verbose_name='사용자 이름')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('auth_num', models.CharField(max_length=8, null=True, verbose_name='인증번호')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
