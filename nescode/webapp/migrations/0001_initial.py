# Generated by Django 2.0.7 on 2019-07-17 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_created=True)),
                ('Name', models.CharField(max_length=30)),
                ('Add', models.CharField(max_length=30)),
                ('Phone_no', models.IntegerField()),
                ('Email', models.CharField(max_length=30)),
            ],
        ),
    ]
