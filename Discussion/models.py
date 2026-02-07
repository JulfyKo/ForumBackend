from django.db import models

# Create your models here.
class Discussion(models.odel):
    theme = models.CharField(max_length=250)
    dateTimeOfCreation = models.DateField()
    userId = models.CharField(max_length=30)

class Comment(models.Model):
    comm = models.CharField()
    dateTimeOfCreation = models.DateField()
    userId = models.CharField(max_length=30)

    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="commentaries")
    
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replies")  