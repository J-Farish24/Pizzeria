from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=50)
    #Sets attribute to current date and timeZone
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        