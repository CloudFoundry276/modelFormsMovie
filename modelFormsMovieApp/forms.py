from django import forms
from modelFormsMovieApp.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
