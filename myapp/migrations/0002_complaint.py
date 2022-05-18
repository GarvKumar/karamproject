# Generated by Django 3.2 on 2021-06-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=10)),
                ('company', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('postalCode', models.CharField(max_length=30)),
                ('itemName', models.CharField(max_length=100)),
                ('itemCode', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='complaint/')),
            ],
        ),
    ]