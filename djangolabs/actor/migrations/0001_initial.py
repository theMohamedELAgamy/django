# Generated by Django 4.0.4 on 2022-06-04 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Actor Name')),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=1)),
                ('profile_image', models.ImageField(upload_to='actor_image')),
            ],
        ),
    ]
