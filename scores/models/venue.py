from django.db import models


class Venue(models.Model):
    def __str__(self):
        return self.venuehistory_set.latest('valid_from').name

    def current_info(self, date):
        return self.groundinfo_set.filter(valid_from__lte=date).latest("valid_from")


class VenueHistory(models.Model):
    class Meta:
        ordering = ["-valid_from"]

    def __str__(self):
        return "{} {}".format(self.valid_from, self.name)

    ground = models.ForeignKey("Venue", on_delete=models.CASCADE)
    valid_from = models.DateField()

    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField(null=True)
