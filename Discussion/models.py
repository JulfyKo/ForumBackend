from django.db import models

# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=30)
    dateTimeOfCreation = models.DateTimeField(auto_now_add=True)

class Discussion(models.Model):
    theme = models.CharField(max_length=250)
    dateTimeOfCreation = models.DateTimeField(auto_now_add=True)
    userId = models.CharField(max_length=30)

    community = models.ForeignKey(Community, on_delete=models.CASCADE)

class Comment(models.Model):    
    comm = models.TextField()
    dateTimeOfCreation = models.DateTimeField(auto_now_add=True)
    userId = models.CharField(max_length=30)

    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="commentaries")
    
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True)  