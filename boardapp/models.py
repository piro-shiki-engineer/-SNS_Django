from django.db import models

class Board_Model(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    snsimg = models.ImageField(upload_to='', blank=True)
    good = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    read_text = models.TextField()
