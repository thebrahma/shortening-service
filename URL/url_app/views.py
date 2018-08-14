from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,Http404
from django.views import View
from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponse
from url_app.models import Url
from url_app import forms
from url_app.utils import create_shortcode
from analytics.models import ClickEvent

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class HomeView(View) :
    def get(self,request, *args, **kwargs):
        form = forms.UrlForm()
        context = {
            'title' : 'URL Shortener',
            'form' : form
        }
        return render(request, 'url_app/home.html', context)

    def post(self,request, *args, **kwargs):
        form = forms.UrlForm(request.POST)
        template = "url_app/home.html"
        context = {
            'title' :'URL Shortener',
            'form' : form
        }
        if form.is_valid() :
            new_url = form.cleaned_data['url']
            print(new_url)
            try:
                obj = Url.objects.get(url = new_url)
                context = {
                    'object' : obj,
                }
                template = "url_app/already-exists.html"
            except Url.DoesNotExist:
                obj = Url(url=new_url)
               # obj.shortcode = create_shortcode(instance=obj)
                obj.save()
                context = {
                    'object' : obj,
                }
                template = "url_app/success.html"
        else :
            print(form.errors)

        return render(request, template, context)

class URLRedirectView(View) :
    def get(self, request, shortcode=None, *args, **kwargs) :
        print("1")
        qs = Url.objects.filter(shortcode__exact = shortcode)
        print("2")
        if qs.count() != 1 and not qs.exists() :
            print(ClickEvent.object.create_event(obj))
            print("3")
            return Http404
        obj = qs.first()
        return HttpResponseRedirect(obj.url)

