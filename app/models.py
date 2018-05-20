from django.db import models

class Users(models.Model):
    username=models.CharField(max_length=50 , default='')
    about=models.CharField(max_length=2000, default='')
    friends = models.ManyToManyField('self',default=None)


    class Meta(object):
        ordering = ['username']

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(Users)
    text = models.CharField(max_length=2000)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes=models.IntegerField(default=0)

    class Meta(object):
        ordering = ['-updated_at', 'text']

    def __str__(self):
        return self.text