# Generated by Django 3.2.25 on 2024-03-09 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_name', models.CharField(max_length=255)),
                ('clinic_logo', models.ImageField(upload_to='clinic_logos/')),
                ('physician', models.CharField(max_length=255)),
                ('physician_contact', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('contact', models.CharField(max_length=20)),
                ('chief_complaint', models.TextField()),
                ('consultation_note', models.TextField()),
            ],
        ),
    ]