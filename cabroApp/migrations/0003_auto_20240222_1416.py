# Generated by Django 3.2.12 on 2024-02-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabroApp', '0002_auto_20240222_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece_jointe',
            name='file',
            field=models.FileField(upload_to='pièces-jointes/'),
        ),
        migrations.AlterField(
            model_name='tache',
            name='date_fin',
            field=models.DateField(null=True),
        ),
    ]
