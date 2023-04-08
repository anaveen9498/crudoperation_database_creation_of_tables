from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self) :
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    player_name=models.CharField(max_length=100)
    url=models.URLField()
    Email=models.EmailField(default='naveen99@gmail.com')

    def __str__(self):
        return self.player_name

class Location(models.Model):
    player_name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    age=models.IntegerField()
    place=models.CharField(max_length=100)
    Date=models.DateField(default='2023-04-08')

    def __str__(self):
        return self.place
