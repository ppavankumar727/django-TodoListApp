# Generated by Django 3.2.4 on 2021-06-30 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('due_date', models.DateTimeField()),
                ('label', models.CharField(choices=[('P', 'primary'), ('S', 'seconda'), ('SU', 'success'), ('D', 'danger')], default='P', max_length=2)),
            ],
        ),
    ]