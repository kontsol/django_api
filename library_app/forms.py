from django import forms

class AuthorSearchForm(forms.Form):
  author_name = forms.CharField(label = "Search author name", max_length=100)