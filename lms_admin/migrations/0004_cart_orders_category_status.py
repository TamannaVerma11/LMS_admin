# Generated by Django 4.2.3 on 2024-02-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_admin', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.IntegerField(default=1),
        ),
    ]
