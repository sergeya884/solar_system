from django.db import models

class CelestialBody(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    is_planet = models.BooleanField(default=True)
    order_from_sun = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
