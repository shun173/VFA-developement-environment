# Generated by Django 2.2.5 on 2020-05-04 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0004_auto_20200501_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecapp.Product'),
        ),
    ]
