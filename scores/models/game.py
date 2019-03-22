from django.db import models


class Game(models.Model):
    def __str__(self):
        return "{} {}-{} {} ({})".format(
            self.home_team.name,
            self.home_goals,
            self.away_goals,
            self.away_team.name,
            self.kickoff.date(),
        )

    season = models.ForeignKey("Season", on_delete=models.CASCADE)
    competition = models.ForeignKey("Competition", on_delete=models.CASCADE)

    kickoff = models.DateTimeField()

    home_team = models.ForeignKey(
        "Team", related_name="home_games", on_delete=models.CASCADE
    )
    away_team = models.ForeignKey(
        "Team", related_name="away_games", on_delete=models.CASCADE
    )

    home_goals = models.PositiveSmallIntegerField()
    away_goals = models.PositiveSmallIntegerField()

    venue = models.ForeignKey("Venue", on_delete=models.CASCADE, null=True)
    attendance = models.PositiveIntegerField(null=True)

    referee = models.ForeignKey("Referee", on_delete=models.CASCADE, null=True)

    home_manager = models.ForeignKey(
        "Manager", related_name="home_appearances", on_delete=models.CASCADE, null=True
    )
    away_manager = models.ForeignKey(
        "Manager", related_name="away_appearances", on_delete=models.CASCADE, null=True
    )


class FriendlyGame(Game):
    pass


class LeagueGame(Game):
    matchday = models.PositiveSmallIntegerField()


class GroupGame(Game):
    matchday = models.PositiveSmallIntegerField()
    group = models.CharField(max_length=2)
    tournament_round = models.PositiveSmallIntegerField()


class KnockoutGame(Game):
    matchday = models.PositiveSmallIntegerField()
    tournament_round = models.PositiveSmallIntegerField()
    following_game = models.ForeignKey("KnockoutGame", null=True, on_delete=models.CASCADE)
