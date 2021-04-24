from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=11)
    desc = models.TextField(max_length=80)

    # this code is for showing name and email on admin panel
    def __str__(self):
        return self.name+" - "+self.email


class Feedback(models.Model):
    comment = models.CharField(max_length=5)
    suggest = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=11)
    desc = models.CharField(max_length=90)


    def __str__(self):
        return self.name





# name jitendra
# email jitendralodhi108@gmail.com
# pwd Jitu@1810