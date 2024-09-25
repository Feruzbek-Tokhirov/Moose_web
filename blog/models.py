from django.db import models


# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=202)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    is_published = models.BooleanField(default=False)

    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
