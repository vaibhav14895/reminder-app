# Generated by Django 4.1.4 on 2023-09-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='times',
            name='eight',
            field=models.CharField(choices=[('7', 'CN lab'), ('5', 'AI'), ('8', 'DAA lab'), ('9', 'null'), ('1', 'HPC'), ('4', 'CN'), ('3', 'DAA'), ('6', 'BIG DATA'), ('2', 'SE')], default='1', max_length=40),
        ),
        migrations.AlterField(
            model_name='times',
            name='eleven',
            field=models.CharField(choices=[('7', 'CN lab'), ('5', 'AI'), ('8', 'DAA lab'), ('9', 'null'), ('1', 'HPC'), ('4', 'CN'), ('3', 'DAA'), ('6', 'BIG DATA'), ('2', 'SE')], default='4', max_length=40),
        ),
        migrations.AlterField(
            model_name='times',
            name='five',
            field=models.CharField(choices=[('7', 'CN lab'), ('5', 'AI'), ('8', 'DAA lab'), ('9', 'null'), ('1', 'HPC'), ('4', 'CN'), ('3', 'DAA'), ('6', 'BIG DATA'), ('2', 'SE')], default='9', max_length=40),
        ),
        migrations.AlterField(
            model_name='times',
            name='four',
            field=models.CharField(choices=[('7', 'CN lab'), ('5', 'AI'), ('8', 'DAA lab'), ('9', 'null'), ('1', 'HPC'), ('4', 'CN'), ('3', 'DAA'), ('6', 'BIG DATA'), ('2', 'SE')], default='9', max_length=40),
        ),
        migrations.AlterField(
            model_name='times',
            name='nine',
            field=models.CharField(choices=[('7', 'CN lab'), ('5', 'AI'), ('8', 'DAA lab'), ('9', 'null'), ('1', 'HPC'), ('4', 'CN'), ('3', 'DAA'), ('6', 'BIG DATA'), ('2', 'SE')], default='2', max_length=40),
        ),
        migrations.AlterField(
            model_name='times',
            name='one',
            field=models.CharField(choices=[('7', 'CN lab'), ('5', 'AI'), ('8', 'DAA lab'), ('9', 'null'), ('1', 'HPC'), ('4', 'CN'), ('3', 'DAA'), ('6', 'BIG DATA'), ('2', 'SE')], default='6', max_length=40),
        ),
        migrations.AlterField(
            model_name='times',
            name='ten',
            field=models.CharField(choices=[('7', 'CN lab'), ('5', 'AI'), ('8', 'DAA lab'), ('9', 'null'), ('1', 'HPC'), ('4', 'CN'), ('3', 'DAA'), ('6', 'BIG DATA'), ('2', 'SE')], default='3', max_length=40),
        ),
        migrations.AlterField(
            model_name='times',
            name='three',
            field=models.CharField(choices=[('7', 'CN lab'), ('5', 'AI'), ('8', 'DAA lab'), ('9', 'null'), ('1', 'HPC'), ('4', 'CN'), ('3', 'DAA'), ('6', 'BIG DATA'), ('2', 'SE')], default='8', max_length=40),
        ),
        migrations.AlterField(
            model_name='times',
            name='twelve',
            field=models.CharField(choices=[('7', 'CN lab'), ('5', 'AI'), ('8', 'DAA lab'), ('9', 'null'), ('1', 'HPC'), ('4', 'CN'), ('3', 'DAA'), ('6', 'BIG DATA'), ('2', 'SE')], default='5', max_length=40),
        ),
        migrations.AlterField(
            model_name='times',
            name='two',
            field=models.CharField(choices=[('7', 'CN lab'), ('5', 'AI'), ('8', 'DAA lab'), ('9', 'null'), ('1', 'HPC'), ('4', 'CN'), ('3', 'DAA'), ('6', 'BIG DATA'), ('2', 'SE')], default='7', max_length=40),
        ),
    ]