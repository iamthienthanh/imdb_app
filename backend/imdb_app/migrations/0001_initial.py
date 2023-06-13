# Generated by Django 4.2.2 on 2023-06-12 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('actor_id', models.AutoField(primary_key=True, serialize=False)),
                ('actor_name', models.CharField(max_length=255)),
                ('biography', models.TextField()),
                ('birthdate', models.CharField(max_length=255)),
                ('birthplace', models.CharField(max_length=255)),
                ('bio_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genre_id', models.AutoField(primary_key=True, serialize=False)),
                ('genre_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=255)),
                ('release_year', models.CharField(max_length=255)),
                ('average_rating', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=255)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_app.movie')),
            ],
        ),
        migrations.CreateModel(
            name='MovieGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_app.genre')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_app.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('award_id', models.AutoField(primary_key=True, serialize=False)),
                ('award_name', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_app.actors')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_app.movie')),
            ],
        ),
        migrations.CreateModel(
            name='ActorMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_app.actors')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imdb_app.movie')),
            ],
        ),
    ]
