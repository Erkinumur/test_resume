# Generated by Django 3.1.2 on 2020-10-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20201011_1846'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resume',
            options={'verbose_name': 'Резюме', 'verbose_name_plural': 'Резюме'},
        ),
        migrations.AlterField(
            model_name='resume',
            name='department',
            field=models.CharField(choices=[('IT', 'IT'), ('Отдел продаж', 'Отдел продаж'), ('Маркетинг', 'Маркетинг')], max_length=50, verbose_name='Направление'),
        ),
    ]
