from django.db import models

# Create your models here.
class Truth(models.Model):
    id=models.IntegerField
    title=models.CharField(max_length=120,blank=True)
    label=models.CharField(max_length=120,blank=True)
    Truth=models.TextField()
    reason=models.TextField()
    
    class Meta:
        ordering=("-label",)

