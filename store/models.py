from django.db import models
from user.models import CustomUser


class Image(models.Model):

    artist = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/')
    name = models.CharField(max_length=25,blank=True)
    description = models.CharField(max_length=250,blank=True,null=True)
    likes = models.PositiveIntegerField(null=True,blank=True)
    slug = models.SlugField(blank=True,null=True)
    category = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.artist.username



