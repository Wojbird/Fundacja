from django.forms import ModelForm
from .models import Chapter
from .models import Picture


class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        fields = '__all__'


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        fields = '__all__'
