# Generated by Django 5.1 on 2024-11-03 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_app', '0008_checkoutitem_boys_checkoutitem_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
