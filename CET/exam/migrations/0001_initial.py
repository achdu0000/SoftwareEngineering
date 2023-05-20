# Generated by Django 4.1 on 2023-05-19 13:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Exam",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("date", models.DateField()),
                ("place", models.CharField(max_length=30)),
                ("max_students", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Paper",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("question_ids", models.CharField(max_length=512)),
                ("type", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("type", models.IntegerField()),
                ("question", models.CharField(max_length=100)),
                ("answer", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="ExamOrder",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("paid", models.BooleanField()),
                ("payment", models.FloatField()),
                ("pay_time", models.DateField(default=django.utils.timezone.now)),
                (
                    "exam",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exam.exam"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="user.student"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="exam",
            name="paper",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="exam.paper"
            ),
        ),
    ]