from django.forms import *


from .models import ProductOpinion


class ProductOpinionForm(ModelForm):
    class Meta:
        model = ProductOpinion
        fields = '__all__'

    rating = IntegerField(min_value=1, max_value=5)
    title = CharField(widget=TextInput(attrs={'placeholder': 'Title of opinion...'}), max_length=250)
    opinion = CharField(widget=Textarea(attrs={'placeholder': 'Opinion...'}), max_length=1500)


