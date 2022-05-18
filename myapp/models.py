from django.db import models


# Create your models here.

class Enquiry(models.Model):
    productCode=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    postalCode=models.CharField(max_length=30)
    company=models.CharField(max_length=100)
    query=models.TextField()
    file=models.FileField(upload_to="enquiry/")
    replyMailSent=models.CharField(max_length=20, default="")

class Complaint(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    company=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    postalCode=models.CharField(max_length=30)
    itemName=models.CharField(max_length=100)
    itemCode=models.CharField(max_length=100)
    file=models.FileField(upload_to="complaint/")
    replyMailSent=models.CharField(max_length=20, default="")

class Feedback(models.Model):
    productQuality=models.CharField(max_length=30)
    productDelivery=models.CharField(max_length=30)
    communication=models.CharField(max_length=30)
    behaviour=models.CharField(max_length=30)
    paperwork=models.CharField(max_length=30)
    packingInnerQuality=models.CharField(max_length=30)
    packingOuterQuality=models.CharField(max_length=30)
    presentationAndCatalogues=models.CharField(max_length=30)
    comment=models.TextField()
    company=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    dealerName=models.CharField(max_length=50)
    goods=models.CharField(max_length=40)
    replyMailSent=models.CharField(max_length=20, default="")