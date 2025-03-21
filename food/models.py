from django.db import models

# Create your models here.
class Item (models.Model):
    # to see item_name on django shell
    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image_link = models.CharField(max_length = 500,default = "https://www.thefuzzyduck.co.uk/wp-content/uploads/2024/05/image-coming-soon-placeholder-01-660x660.png")

    