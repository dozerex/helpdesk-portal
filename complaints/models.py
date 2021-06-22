from django.core import validators
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.


class Complaint(models.Model):
    title = models.CharField(max_length=40)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="complaints")
    urgency = models.IntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    location = models.CharField(max_length=20, default="Hostel")
    image = models.ImageField(upload_to="images")
    text = models.TextField(max_length=300, null=True)
    date = models.DateField(auto_now=True)
    is_solved = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])

    def __str__(self):
        return f"{self.title} (Severity:{self.urgency})"
