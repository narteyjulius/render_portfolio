from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    # contact_name = forms.CharField(required=True)
    # contact_email = forms.EmailField(required=True)
    # content = forms.CharField(
    #     required=True,
    #     widget=forms.Textarea
    # )