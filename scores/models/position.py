from django.db import models


class Position(models.Model):
    def __str__(self):
        return self.code

    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)
    sort_order = models.SmallIntegerField()


class Lineup(models.Model):
    class Meta:
        indexes = [models.Index(fields=["player", "game", "team"])]
        unique_together = ("player", "game")

    def __str__(self):
        return "{} {}".format(player, self.game)

    player = models.ForeignKey("Player", on_delete=models.CASCADE, db_index=True)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, db_index=True)
    team = models.ForeignKey("Team", on_delete=models.CASCADE, db_index=True)

    position = models.ForeignKey("Position", null=True, on_delete=models.SET_NULL)
    is_captain = models.BooleanField(default=True)


class Squad(models.Model):
    class Meta:
        unique_together = ("competition", "season", "team", "player")

    def __str__(self):
        return "{} {} {}".format(self.season, self.team, self.player)

    competition = models.ForeignKey("Competition", on_delete=models.CASCADE)
    season = models.ForeignKey("Season", on_delete=models.CASCADE)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    player = models.ForeignKey("Player", on_delete=models.CASCADE)

    position = models.ForeignKey("Position", null=True, on_delete=models.SET_NULL)
    number = models.PositiveSmallIntegerField(null=True)
