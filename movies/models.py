from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img_path = models.CharField(max_length=255)
    duration = models.IntegerField()
    genre = models.JSONField()  # Stores genres as a list
    language = models.CharField(max_length=50)
    mpaa_rating_type = models.CharField(max_length=10)
    mpaa_rating_label = models.CharField(max_length=255, blank=True, null=True)
    user_rating = models.IntegerField()

    def __str__(self):
        return self.name