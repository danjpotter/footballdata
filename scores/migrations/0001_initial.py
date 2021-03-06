# Generated by Django 2.0.10 on 2019-03-22 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_knockout', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kickoff', models.DateTimeField()),
                ('home_goals', models.PositiveSmallIntegerField()),
                ('away_goals', models.PositiveSmallIntegerField()),
                ('attendance', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('known_as', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(null=True)),
                ('alt_nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alt_scores_manager_related', to='scores.Country')),
                ('nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scores_manager_related', to='scores.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('known_as', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(null=True)),
                ('alt_nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alt_scores_player_related', to='scores.Country')),
                ('nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scores_player_related', to='scores.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=3)),
                ('sort_order', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('known_as', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(null=True)),
                ('alt_nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alt_scores_referee_related', to='scores.Country')),
                ('nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scores_referee_related', to='scores.Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.PositiveSmallIntegerField()),
                ('end_year', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('is_national', models.BooleanField(default=False)),
                ('sorttext', models.CharField(max_length=50)),
                ('website', models.URLField(null=True)),
                ('colours', models.CharField(max_length=50, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scores.Country')),
            ],
        ),
        migrations.CreateModel(
            name='TeamHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('crest', models.ImageField(null=True, upload_to='')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scores.Team')),
            ],
            options={
                'ordering': ['-valid_from'],
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='VenueHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateField()),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('capacity', models.PositiveIntegerField(null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scores.Country')),
                ('ground', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scores.Venue')),
            ],
            options={
                'ordering': ['-valid_from'],
            },
        ),
        migrations.CreateModel(
            name='FriendlyGame',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scores.Game')),
            ],
            bases=('scores.game',),
        ),
        migrations.CreateModel(
            name='GroupGame',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scores.Game')),
                ('matchday', models.PositiveSmallIntegerField()),
                ('group', models.CharField(max_length=2)),
                ('tournament_round', models.PositiveSmallIntegerField()),
            ],
            bases=('scores.game',),
        ),
        migrations.CreateModel(
            name='KnockoutGame',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scores.Game')),
                ('matchday', models.PositiveSmallIntegerField()),
                ('tournament_round', models.PositiveSmallIntegerField()),
                ('following_game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scores.KnockoutGame')),
            ],
            bases=('scores.game',),
        ),
        migrations.CreateModel(
            name='LeagueGame',
            fields=[
                ('game_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='scores.Game')),
                ('matchday', models.PositiveSmallIntegerField()),
            ],
            bases=('scores.game',),
        ),
        migrations.AddField(
            model_name='game',
            name='away_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='away_appearances', to='scores.Manager'),
        ),
        migrations.AddField(
            model_name='game',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_games', to='scores.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='competition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scores.Competition'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='home_appearances', to='scores.Manager'),
        ),
        migrations.AddField(
            model_name='game',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_games', to='scores.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='referee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scores.Referee'),
        ),
        migrations.AddField(
            model_name='game',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scores.Season'),
        ),
        migrations.AddField(
            model_name='game',
            name='venue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scores.Venue'),
        ),
        migrations.AddField(
            model_name='competition',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scores.Country'),
        ),
    ]
