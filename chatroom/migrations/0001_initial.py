# Generated by Django 4.0 on 2024-04-29 02:12

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('creater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_creater', to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=75, scale=0.5, size=None, upload_to='images')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='chatroom.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatUser', to='auth.user')),
            ],
        ),
    ]
