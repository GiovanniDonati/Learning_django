# Generated by Django 5.1.3 on 2024-12-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField(blank=True, null=True)),
                ('data_nascimento', models.DateField()),
                ('is_ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
