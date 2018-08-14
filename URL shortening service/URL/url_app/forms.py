from django import forms
from url_app.validators import validate_dot_com,validate_url

class UrlForm(forms.Form) :
    url = forms.CharField(label='Submit URL',
                          validators=[validate_url, validate_dot_com],
                          widget = forms.TextInput(
                              attrs={
                                  "placeholder": "Long URL",
                                  "class": "form-control"
                              }
                          )
                          )