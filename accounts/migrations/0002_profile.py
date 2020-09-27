# Generated by Django 3.1.1 on 2020-09-26 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('religion', models.CharField(max_length=30)),
                ('mother_tongue', models.CharField(choices=[('TE', 'telugu'), ('EN', 'english'), ('HI', 'hindi'), ('TL', 'tamil')], max_length=2)),
                ('caste', models.CharField(choices=[('HN', 'hindu'), ('MS', 'muslim')], max_length=2)),
                ('gothram', models.CharField(max_length=40)),
                ('dosham', models.CharField(choices=[('NO', 'no'), ('YS', 'yes'), ('DK', 'dontknow')], max_length=2)),
                ('marital_status', models.CharField(choices=[('NM', 'never_married'), ('WD', 'windowed'), ('DI', 'diverced'), ('AD', 'awaiting_diverce')], max_length=3)),
                ('height', models.CharField(choices=[('5', '5_ft'), ('6', '6_ft')], max_length=3)),
                ('family_status', models.CharField(choices=[('MC', 'middle class'), ('UMC', 'upeer middle class'), ('RH', 'rich'), ('AE', 'affluent')], max_length=3)),
                ('family_type', models.CharField(choices=[('JT', 'joint'), ('NR', 'nuclear')], max_length=3)),
                ('family_values', models.CharField(choices=[('OX', 'orthodox'), ('TRL', 'traditional'), ('MRT', 'moderate'), ('LRL', 'liberal')], max_length=3)),
                ('any_diability', models.CharField(choices=[('NL', 'normal'), ('PHD', 'physically challanged')], max_length=3)),
                ('about_you', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
