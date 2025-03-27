from django.db import models

# Create your models here.
class Group(models.Model):
    def __str__(self):
        return self.cate_name
    cate_name = models.CharField(max_length=200)
    cate_desc = models.TextField()

