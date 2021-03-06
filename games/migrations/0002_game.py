# Generated by Django 2.2.8 on 2019-12-26 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('category', models.ManyToManyField(related_name='games', to='games.GameCategory')),
            ],
        ),
    ]
