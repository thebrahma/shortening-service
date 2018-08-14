from django.conf import settings
from django.db import models
from url_app import utils
from url_app.validators import  validate_url, validate_dot_com

#from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse
# Create your models here.

SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX",15)
SHORTCODE_MIN = getattr(settings,"SHORTCODE_MIN",5)

class Url(models.Model) :
    url = models.CharField(max_length=228, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, blank=True, unique=True)
    updated = models.DateTimeField(auto_now=True) #every time the model is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when the model is created

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode =="" :
            self.shortcode = utils.create_shortcode(self)
        super(Url, self).save(*args,**kwargs)

    def __str__(self) :
        return self.url

    def get_short_url(self):
        #return "http://www.utpal.com/{shortcode}".format(shortcode=self.shortcode)
        url_path = reverse("scode", kwargs={'shortcode' : self.shortcode},host='www', scheme='http')
        return url_path