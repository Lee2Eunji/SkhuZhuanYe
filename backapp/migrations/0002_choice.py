# Generated by Django 4.1.2 on 2022-10-12 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('developer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backapp.developer')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backapp.question')),
            ],
        ),
    ]
