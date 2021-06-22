from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", max_length=128, widget=forms.PasswordInput)


class ComplaintForm(forms.Form):
    title = forms.CharField(label="Title", max_length=40)
    urgency = forms.IntegerField(label="Severity", min_value=1, max_value=5)
    location = forms.CharField(label="Location", max_length=20)
    image = forms.ImageField()
    text = forms.CharField(max_length=300,widget=forms.Textarea)

