# Generated by Django 4.2.5 on 2023-09-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('valor', models.FloatField()),
                ('data_de_validade', models.DateTimeField(blank=True, null=True)),
                ('quantidade', models.IntegerField(default=0)),
                ('quantidade2', models.IntegerField(default=0)),
            ],
        ),
    ]
