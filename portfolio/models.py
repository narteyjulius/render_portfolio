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

class Touch(models.Model):
    lead = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)


class Project(models.Model):
    description = models.TextField(max_length=500, blank=True)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True)
    link = models.URLField(blank=True)
    gitlink = models.URLField(blank=True)

    def __str__(self):
        return self.title