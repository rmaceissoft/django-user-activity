from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class ActivityType(models.Model):
    keyname = models.SlugField(max_length=100, unique=True)
    label = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Activity Type"
        verbose_name_plural = "Activity Types"
        
    def __unicode__(self): return self.label
    
    
class Activity(models.Model):
    user = models.ForeignKey(User)
    activity_type = models.ForeignKey(ActivityType)
    timestamp = models.DateTimeField(default=datetime.now, editable=False, blank=True)
    hits = models.PositiveSmallIntegerField(default=1) #used when
    
    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
         
