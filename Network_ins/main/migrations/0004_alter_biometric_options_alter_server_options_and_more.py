# Generated by Django 4.0 on 2023-04-20 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_cameras_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biometric',
            options={'verbose_name_plural': 'Biometrics'},
        ),
        migrations.AlterModelOptions(
            name='server',
            options={'verbose_name_plural': 'Servers'},
        ),
        migrations.AlterModelOptions(
            name='switch',
            options={'verbose_name_plural': 'Switches'},
        ),
        migrations.AlterModelOptions(
            name='vlan',
            options={'verbose_name_plural': 'Vlans'},
        ),
        migrations.AlterModelOptions(
            name='wifi',
            options={'verbose_name_plural': 'Wifi'},
        ),
    ]
