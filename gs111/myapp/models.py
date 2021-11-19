from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class User1(models.Model):

    username = models.CharField(max_length=70,default=None)
    password = models.IntegerField(default=None)

    def __str__(self):
        return self.username

    

    
class Post(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.PROTECT)
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user = models.OneToOneField(User, on_delete=models.PROTECT)
    user = models.OneToOneField(User1, on_delete=models.SET_NULL, null=True)

    post_title =  models.CharField(max_length=70,default=None)
    post_cat =  models.CharField(max_length=70,default=None)
    post_publish_date =  models.DateField(default=None)
