from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# class transportprotocol(models.Model):
#     trans_protocol=models.CharField(max_length=200, null=True, blank=True)

#     def __str__(self):
#         return self.trans_protocol

class Wireless(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    ipaddress=models.CharField(max_length=200)
    transportprotocol=models.CharField(max_length=100)
    #transpor_protocol=models.ForeignKey(transportprotocol, on_delete=models.CASCADE)


    def __str__(self):
        return self.username