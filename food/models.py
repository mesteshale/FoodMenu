from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from group.models import Group
# Create your models here.
class Item (models.Model):
    # to see item_name on django shell
    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image_link = models.CharField(max_length = 500,default = "https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")

    # Add ForeignKey to Group model
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='items', default=5)  # ForeignKey to Group

    def get_absolute_url(self):
        return reverse('food:detail',kwargs={'pk':self.pk})
