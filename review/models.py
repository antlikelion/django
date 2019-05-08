from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    review = models.TextField()
    BEST = "☆☆☆☆☆"
    GOOD = "☆☆☆☆"
    SOSO = "☆☆☆"
    BAD = "☆☆"
    WORST = "☆"
    SCORE_CHOICES = (
        (BEST, "☆☆☆☆☆"),
        (GOOD, "☆☆☆☆"),
        (SOSO, "☆☆☆"),
        (BAD, "☆☆"),
        (WORST, "☆"),
    )
    score = models.CharField(
        max_length=5,
        choices=SCORE_CHOICES,
        # default=SOSO,
    )
    price = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    writer = models.CharField(max_length=200)
    publisher = models.CharField(
        max_length=20,
    )

    img = models.FileField(null=True)

    # image = models.ImageField(upload_to="profile_image", blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
