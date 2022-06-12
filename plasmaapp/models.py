from datetime import datetime
from distutils.command.upload import upload
import email
import os
from unicodedata import name
from django.db import models


# Create your models here.


def file(request,filename):
 original_filename = filename
 nowTime =datetime.now().strftime('%Y%m%d%H:%M:%S')
 filename = "%s%s" % (nowTime,original_filename)
 return os.path.join('uploads/',filename)


class contact(models.Model):
 id = models.AutoField(primary_key=True) 
 name = models.CharField(max_length=20)
 email = models.CharField(max_length=20)
 subject = models.CharField(max_length=30)
 messages = models.TextField()
 
 def __str__(self):
  return self.name
 
 
class registration_details(models.Model):
   
  unique_id = models.AutoField(primary_key=True)
  team_name = models.CharField(max_length=25)
  member1_name = models.CharField(max_length=20)
  member1_email = models.EmailField()
  member1_phone = models.TextField()
  member1_college = models.TextField()
  member1_branch = models.CharField(max_length=40)
  member2_name = models.CharField(max_length=20)
  member2_email = models.EmailField()
  member2_phone = models.TextField()
  member2_college = models.TextField()
  member2_branch = models.CharField(max_length=40)
  member3_name = models.CharField(max_length=20)
  member3_email = models.EmailField()
  member3_phone = models.TextField()
  member3_college = models.TextField()
  member3_branch = models.CharField(max_length=40)
  member4_name = models.CharField(max_length=20)
  member4_email = models.EmailField()
  member4_phone = models.TextField()
  member4_college = models.TextField()
  member4_branch = models.CharField(max_length=40)
  total_amount = models.CharField(max_length=8)
  selected_event = models.TextField()
  hospitality = models.TextField()
  
  
  def __str__(self):
   return self.team_name
 
class payment(models.Model):
  member1_name = models.CharField(max_length=20)
  member1_email = models.EmailField()
  member1_phone = models.TextField()
  member1_college = models.TextField()
  member1_branch = models.CharField(max_length=40)
  paid_amount = models.IntegerField()
  payment_mode = models.TextField()
  payment_date =  models.DateField()
  paid_by = models.TextField()
  utr_upi_no = models.TextField()
  screenshot = models.ImageField(upload_to=file,null=True,blank=True)
  
  
  def __str__(self):
    return self.member1_name