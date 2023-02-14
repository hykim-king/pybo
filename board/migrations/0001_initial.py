# Generated by Django 4.0.3 on 2023-02-14 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('create_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'board',
                'managed': False,
            },
        ),
    ]
