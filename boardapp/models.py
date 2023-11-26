from django.db import models

class Board_Model(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    snsimg = models.ImageField(upload_to='')
    good = models.IntegerField()
    read = models.IntegerField()
    read_text = models.TextField()
