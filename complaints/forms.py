from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(
        label="Password", max_length=128, widget=forms.PasswordInput)


class ComplaintForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    urgency = forms.IntegerField(label="Severity", min_value=1, max_value=5)
    location = forms.CharField(label="Location", max_length=20)
    image = forms.ImageField()
    text = forms.CharField(max_length=300, widget=forms.Textarea)


class ProfileForm(forms.Form):
    first_name = forms.CharField(
        label="First Name", max_length=50, required=False)
    last_name = forms.CharField(
        label="Last Name", max_length=50, required=False)
    email = forms.EmailField(label="Email", required=False)
    dob = forms.DateField(label="Date of Birth", required=False)
    phone = forms.CharField(label="Phone NO", max_length=10, required=False)
    department = forms.ChoiceField(choices=(
        ("CSE", "Computer Science Engineering"),
        ("CSAI", "Computer Science in Artificial Inteligence"),
        ("IT", "Information Technology"),
        ("DS", "Data Science"),
        ("AI", "Artificial Inteligence"),
        ("CN", "Computer Networking")), required=False)
    degree = forms.ChoiceField(choices=(
        ("B.Tech", "Bachelor of Technology"),
        ("M.Tech", "Master of Technology"),
        ("PhD", "Doctor of Philosophy")), required=False)
