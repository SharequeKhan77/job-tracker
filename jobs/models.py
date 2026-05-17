from django.db import models

# Create your models here.

class Job(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('rejected', 'Rejected'),
        ('offer', 'Offer'),
    ])
    date_applied = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.position} at {self.company}"