from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    health_conditions = models.TextField()

class HealthData(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    data = models.JSONField()  # Storing health data in JSON format
    timestamp = models.DateTimeField(auto_now_add=True)

