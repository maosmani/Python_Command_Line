from django.forms import ModelForm
from .models import List , Tutorials

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = ['name','email']

class TutorialsForm(ModelForm):
    class Meta:
        model = Tutorials
        fields = ['title','body','author']
