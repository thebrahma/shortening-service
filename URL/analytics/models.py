from django.db import models

# Create your models here.

from url_app.models import Url

class ClickEventManager(models.Manager) :
    def create_event(self, instance):
        if isinstance(instance, Url) :
            obj, created = self.get_or_create(kirr_url=instance)
            obj.count +=1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model) :
    analytics_url = models.OneToOneField(Url)
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True) #every time the model is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when the model is created

    object = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)
