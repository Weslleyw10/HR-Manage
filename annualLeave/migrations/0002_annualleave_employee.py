# Generated by Django 3.2.2 on 2021-05-19 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
        ('annualLeave', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='annualleave',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee.employee'),
        ),
    ]