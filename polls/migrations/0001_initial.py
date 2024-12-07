# Generated by Django 5.1.2 on 2024-11-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diabetes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.BigIntegerField()),
                ('glucose', models.BigIntegerField()),
                ('bloodPressure', models.BigIntegerField()),
                ('skinThickness', models.BigIntegerField()),
                ('insulin', models.BigIntegerField()),
                ('bmi', models.BigIntegerField()),
                ('diabetesPedigreeFunction', models.BigIntegerField()),
                ('age', models.BigIntegerField()),
                ('outcome', models.BigIntegerField()),
            ],
        ),
    ]
