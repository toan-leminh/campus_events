from django.db import models
from django.forms import ValidationError

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    approved_at = models.DateTimeField(null=True, blank=True)

    def clean(self):
        super().clean()
        # Validate end_datetime is later than start_datetime    
        if self.end_datetime < self.start_datetime:
            raise ValidationError('End datetime must be later than start datetime')



