# Generated by Django 3.2.16 on 2023-01-05 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_remove_skill_score'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Testimonial',
        ),
    ]