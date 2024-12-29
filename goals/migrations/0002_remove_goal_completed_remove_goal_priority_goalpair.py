# Generated by Django 5.1.1 on 2024-12-29 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='goal',
            name='priority',
        ),
        migrations.CreateModel(
            name='GoalPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False)),
                ('goal1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal1_pairs', to='goals.goal')),
                ('goal2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal2_pairs', to='goals.goal')),
            ],
            options={
                'unique_together': {('goal1', 'goal2')},
            },
        ),
    ]