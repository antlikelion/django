from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    review = models.TextField()
    GOOD = "GOOD"
    SOSO = "SOSO"
    BAD = "BAD"
    SCORE_CHOICES = (
        (GOOD, "Good"),
        (SOSO, "So so"),
        (BAD, "Bad"),
    )
    score = models.CharField(
        max_length=4,
        choices=SCORE_CHOICES,
        default=SOSO,
    )
    price = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    def is_upperclass(self):
        return self.score in (self.GOOD, self.SOSO, self.BAD)

    def __str__(self):
        return self.title
