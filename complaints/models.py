from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

from django.db.models.signals import post_save

# Create your models here.


class Complaint(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="complaints")
    urgency = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    location = models.CharField(max_length=20, default="Hostel")
    image = models.ImageField(upload_to="images")
    text = models.TextField(max_length=300, null=True)
    date = models.DateField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])

    def __str__(self):
        return f"{self.title} (Severity:{self.urgency})"


class ProfileModel(models.Model):
    username = models.CharField(max_length=50)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    # batch = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} : {self.first_name}  {self.last_name} : {self.department}"


def create_update_profile(sender, instance, created, **kwargs):
    if created:
        ProfileModel.objects.create(
            user=instance,
            username=instance.username
        )
        print("profile created")
    else:
        instance.profile.save()
        print("update profile")


post_save.connect(create_update_profile, sender=User)
