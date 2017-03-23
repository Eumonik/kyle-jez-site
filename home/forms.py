from django import forms

class SearchForm(forms.Form):
    search_box = forms.CharField(label='Search', max_length=40)

class ContactForm(forms.Form):
    contact_name = forms.CharField(
        required=True,
        label='Name',
        widget=forms.TextInput(attrs={'size': '40','class':'contab'}),
        )
    contact_email = forms.EmailField(
        required=True,
        label='Email',
        widget=forms.TextInput(attrs={'size': '40','class':'contab'}),
        )
    contact_message = forms.CharField(
        required=True,
        label='Message',
        widget=forms.Textarea(attrs={'class':'contab'}),
        )
