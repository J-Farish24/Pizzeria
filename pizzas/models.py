from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=50)
    #Sets attribute to current date and timeZone
    date_created = models.DateTimeField(auto_now_add=True)
    #Stores image for a Pizza object
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_created']
    
    def __str__(self):
        return self.text