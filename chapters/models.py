from django.db import models


# Create your models here.
class Chapter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        # ordering = ['id']

    def __str__(self):
        return self.name


class Picture(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    img = models.BinaryField(null=True, blank=True)

    class Meta:
        ordering = ['name']
        # ordering = ['id']

    def __str__(self):
        return self.name
