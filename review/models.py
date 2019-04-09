from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    review = models.TextField()
    BEST = "5"
    GOOD = "4"
    SOSO = "3"
    BAD = "2"
    WORST = "1"
    SCORE_CHOICES = (
        (BEST, "5"),
        (GOOD, "4"),
        (SOSO, "3"),
        (BAD, "2"),
        (WORST, "1"),
    )
    score = models.CharField(
        max_length=1,
        choices=SCORE_CHOICES,
        default=SOSO,
    )
    price = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

    # def is_upperclass(self):
    #     return self.score in (self.GOOD, self.SOSO, self.BAD)

    def __str__(self):
        return self.title

    # def __str__(self):
    #     return self.review

    # def __str__(self):
    #     return self.score

    # def __str__(self):
    #     return self.price
