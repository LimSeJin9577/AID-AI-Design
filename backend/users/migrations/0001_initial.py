# Generated by Django 3.2 on 2022-02-09 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(db_column='phone_no', default='', max_length=100, null=True)),
                ('name', models.CharField(blank=True, db_column='name', max_length=100, null=True)),
                ('user_type', models.CharField(blank=True, db_column='user_type', max_length=100, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
