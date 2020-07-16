from django import forms

class NewEntryForm(forms.Form):
    title = forms.CharField(label='Title', max_length=60)
    content = forms.CharField(label='Content',
                              widget= forms.Textarea(attrs={'style': 'height: 200px;width:500px'}))
    #editTitle = forms.CharField(label='Title', max_length=60, required=True)