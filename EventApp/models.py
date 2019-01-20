from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.


#Abstract User , it is the extension of the base User model which can be customized
class MyUser(AbstractUser):

  def __str__(self):
     return self.username

#RoleMaster contains all the vaarious roles of users
class RoleMaster (models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name

#RoleAssignment assigns the roles to the user
class RoleAssignment (models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    role = models.ForeignKey(RoleMaster, on_delete=models.PROTECT)

    def __int__(self):
        return self.role.name


# model for Department
class Department(models.Model):
    dep_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.TextField()
    img = models.CharField(max_length=200)
    link_to = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# EventMaster to handle the events section
class EventMaster(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=100)
    num_of_winners = models.IntegerField()
    team_size = models.IntegerField()
    entry_fee = models.IntegerField()
    objective = models.TextField(max_length=1000, blank=True)
    rounds = models.TextField(max_length=10000, blank=True)
    rules = models.TextField(max_length=100000, blank=True)

    def __str__(self):
        return self.event_name



class EventDepartment(models.Model):
    event = models.ForeignKey(EventMaster, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.event.event_name

#sponsors model
class SponsorMaster(models.Model):
    sponsor_name = models.CharField(max_length=30)
    sponsor_logo = models.CharField(max_length=200)
    sponsor_info = models.CharField(max_length=200, default='No Info. Available')

    def __str__(self):
        return self.sponsor_name

#contains media for front-end
class Carousel(models.Model):
    src = models.CharField(max_length=200)

#ContactUs contains fields for user Services to contact to admin (Foreign Key to Dept)
class ContactUs(models.Model):

    class Meta:
        verbose_name_plural= "Contact Us"

    user_name = models.CharField(max_length=30)
    user_id = models.EmailField()
    category = models.ForeignKey(Department, on_delete =models.PROTECT, null=True,blank = True)
    user_message = models.CharField(max_length=300)

    def __str__(self):
        return self.user_name
