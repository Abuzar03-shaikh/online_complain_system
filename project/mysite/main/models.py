from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('Electric', 'Electric'),
        ('Plumbing', 'Plumbing'),
        ('Water Supply', 'Water Supply'),
        # add more if needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')  # ✅ check this
    created_at = models.DateTimeField(auto_now_add=True)  # ✅ auto set timestamp

    def __str__(self):
        return f"{self.user.username} - {self.category}"
