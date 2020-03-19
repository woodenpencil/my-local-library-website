from django import forms

def FragmentForm(forms.Form):
	fragment = forms.CharField(label="fragment", max_length=200)
	