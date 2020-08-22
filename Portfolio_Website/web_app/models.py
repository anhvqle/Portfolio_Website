from django.db import models

class Employer(models.Model):
    name = models.CharField(max_length = 128)
    company = models.CharField(max_length = 128)
    position = models.CharField(max_length = 128)
    email = models.EmailField(max_length = 264, unique = True)
    message = models.TextField()

    def __str__(self):
        return self.name

