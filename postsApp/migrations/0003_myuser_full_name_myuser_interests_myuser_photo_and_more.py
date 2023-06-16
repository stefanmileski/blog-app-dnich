# Generated by Django 4.2.2 on 2023-06-16 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postsApp', '0002_alter_myuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='myuser',
            name='interests',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploaded_files/'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='profession',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='myuser',
            name='skills',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='blocked_users',
            field=models.ManyToManyField(blank=True, related_name='blocked_by', to='postsApp.myuser'),
        ),
    ]
