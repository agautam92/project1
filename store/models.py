from django.db import models
from user.models import CustomUser


class Image(models.Model):

    artist = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=25,blank=True)
    description = models.CharField(max_length=250,blank=True,null=True)
    likes = models.PositiveIntegerField()
    slug = models.SlugField()
    category = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name + "BY" + self.artist



