# Generated by Django 2.0.7 on 2018-08-24 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_dept', models.SlugField()),
                ('crs_name', models.CharField(max_length=200)),
                ('crs_num', models.IntegerField(default=100)),
                ('crs_avail', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.CharField(max_length=7)),
                ('dept_full', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GradeVisual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen_year_qtr', models.IntegerField(default=99999)),
                ('visualization', models.CharField(max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseInfo')),
            ],
        ),
        migrations.AddField(
            model_name='courseinfo',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Department'),
        ),
    ]