from django.db import models


class Person(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return self.known_as

    name = models.CharField(max_length=50)
    known_as = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    nationality = models.ForeignKey(
        "Country",
        related_name="%(app_label)s_%(class)s_related",
        on_delete=models.CASCADE,
        null=True,
    )
    alt_nationality = models.ForeignKey(
        "Country",
        related_name="alt_%(app_label)s_%(class)s_related",
        on_delete=models.CASCADE,
        null=True,
    )


class Player(Person):
    pass


class Referee(Person):
    pass


class Manager(Person):
    pass


class Position(models.Model):
    def __str__(self):
        return self.code

    name = models.CharField(max_length=20)
    code = models.CharField(max_length=3)
    sort_order = models.SmallIntegerField()
