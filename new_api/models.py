from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=10)
    mobile_number=models.CharField(max_length=10)
    user_number = models.IntegerField(default=111)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=10)
    price=models.IntegerField()
    item_number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    
    def __str__(self):
     return self.name
 
 
class CustomerReview(models.Model):
    customer_name = models.CharField(max_length=50)
    review_text = models.TextField()
    rating = models.IntegerField()  # Assuming a rating scale (e.g., 1 to 5)
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="review")
    def __str__(self):
        return f"{self.customer_name}'s Review"





