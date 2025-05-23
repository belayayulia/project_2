# Generated by Django 4.1.7 on 2025-05-21 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100, verbose_name='ФИО студента')),
                ('program_name', models.CharField(max_length=100, verbose_name='Название программы')),
                ('year', models.PositiveIntegerField(verbose_name='Год поступления')),
                ('score', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Балл')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Программа',
                'verbose_name_plural': 'Программы',
            },
        ),
    ]
