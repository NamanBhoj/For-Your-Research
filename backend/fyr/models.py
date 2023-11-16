from django.db import models

# Create your models here.
class Paper(models.Model):
    title = models.CharField(max_length=300)
    link = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title
    