from django.db import models


class User(models.Model):
    username=models.CharField(max_length=50)
    about=models.CharField(max_length=2000)
    friends = models.ManyToManyField('self',default=None)

    class Meta(object):
        ordering = ['username']

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.CharField(max_length=2000)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes=models.IntegerField(default=0)

    class Meta(object):
        ordering = ['-posted_at', 'text']

    def __str__(self):
        return self.text