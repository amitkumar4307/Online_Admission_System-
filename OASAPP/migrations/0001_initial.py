# Generated by Django 5.1 on 2024-09-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='answer',
            fields=[
                ('Aid', models.IntegerField(primary_key=True, serialize=False)),
                ('answer', models.CharField(max_length=255)),
                ('anserby', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='enquiry',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=255)),
                ('contactno', models.CharField(max_length=10)),
                ('emailaddress', models.CharField(max_length=50)),
                ('enquirytext', models.CharField(max_length=255)),
                ('enquirydate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('usertype', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='material',
            fields=[
                ('ids', models.AutoField(primary_key=True, serialize=False)),
                ('program', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=100)),
                ('file_name', models.CharField(max_length=255)),
                ('my_file', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='news',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('newstext', models.CharField(max_length=255)),
                ('newsdate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='program',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='question',
            fields=[
                ('Qid', models.IntegerField(primary_key=True, serialize=False)),
                ('questions', models.CharField(max_length=255)),
                ('postby', models.CharField(max_length=50)),
                ('postdate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='response',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('program', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=10)),
                ('emailaddress', models.CharField(max_length=50)),
                ('responsetype', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=500)),
                ('responsetext', models.CharField(max_length=1000)),
                ('responsedate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('fname', models.CharField(max_length=50)),
                ('Mname', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=255)),
                ('program', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.CharField(max_length=50)),
                ('contactno', models.CharField(max_length=10)),
                ('emailaddress', models.CharField(max_length=50)),
                ('regdate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='year',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.CharField(max_length=50)),
            ],
        ),
    ]
