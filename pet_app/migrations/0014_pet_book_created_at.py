# Generated by Django 5.1 on 2024-11-03 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0013_pet_book_balance_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet_book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
