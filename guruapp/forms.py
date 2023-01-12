from django import forms
from django.forms import CharField
from guruapp.models import pmodel

class pform(forms.Form):
	path = forms.FileField()
	class Meta:
		model = pmodel
		fields = ['ccode','scode','ttid','descp','path']
