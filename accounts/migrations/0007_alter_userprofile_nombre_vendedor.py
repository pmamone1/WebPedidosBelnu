# Generated by Django 4.0.5 on 2022-07-08 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nombre_vendedor',
            field=models.CharField(blank=True, default='deposito', max_length=50, unique=True, verbose_name='Nombre de vendedor'),
        ),
    ]