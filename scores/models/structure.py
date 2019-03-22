from django.db import models


class Country(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)


class Competition(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=50)
    country = models.ForeignKey("Country", on_delete=models.CASCADE, null=True)

    is_knockout = models.BooleanField(default=False)


class Season(models.Model):
    def __str__(self):
        if self.start_year == self.end_year:
            return str(self.start_year)
        else:
            return "{}/{}".format(self.start_year, self.end_year)

    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField()
