from .models import Movie
from django import forms
from django.forms import ModelForm



class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
    #
    # def clean(self):
    #     pass

    # def clean_rating(self):
    #     rating = self.cleaned_data['rating']
    #     if rating < 1:
    #         raise forms.ValidationError("Rating cannot be less than 1")
    #     return rating
    #
    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) < 2:
    #         raise forms.ValidationError("Title cant be of single character")
    #     return title

