# Generated by Django 4.1.2 on 2023-01-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=b'I01\n')),
                ('reviewer_pic', models.ImageField(blank=b'I01\n', null=b'I01\n', upload_to='images/')),
                ('body', models.TextField(null=b'I01\n')),
            ],
        ),
    ]