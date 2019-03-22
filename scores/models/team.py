from django.db import models


class Team(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)

    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    is_national = models.BooleanField(default=False)

    sorttext = models.CharField(max_length=50)
    website = models.URLField(null=True)
    colours = models.CharField(max_length=50, null=True)


class TeamHistory(models.Model):
    class Meta:
        ordering = ["-valid_from"]

    def __str__(self):
        return "{} {} {}".format(self.team.name, self.valid_from, self.name)

    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    valid_from = models.DateField()

    name = models.CharField(max_length=50)
    crest = models.ImageField(null=True)
