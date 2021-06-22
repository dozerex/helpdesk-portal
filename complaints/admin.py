from complaints.models import Complaint
from django.contrib import admin
from .models import Complaint


# Register your models here.
class ComplaintAdmin(admin.ModelAdmin):
    list_filter = ("user","urgency","date",)
    list_display = ("title", "urgency",)

admin.site.register(Complaint, ComplaintAdmin)