from django.db import models

# Create your models here.
class Plan(models.Model):
    mission=models.CharField(max_length=200)
    def __unicode__(self):
        return self.mission
