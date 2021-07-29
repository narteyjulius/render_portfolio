from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=50)
    intro = models.CharField(max_length=200, blank=True)
    intor_image = models.ImageField(blank=True)
    skill_name = models.CharField(max_length=50, blank= True)
    profile = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True)
    about = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.name
