# Generated by Django 4.2.3 on 2024-02-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_admin', '0004_cart_orders_category_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.FileField(null=True, upload_to='category/'),
        ),
    ]
