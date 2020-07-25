# Generated by Django 2.2.5 on 2020-05-01 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0002_auto_20200428_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='pub_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='good',
            old_name='pushed_date',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='article',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='ecapp.Product'),
        ),
    ]
