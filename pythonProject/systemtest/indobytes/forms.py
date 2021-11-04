from django import forms


class UserDetailsForm(forms.Form):
    name = forms.CharField(max_length=20)
    mobile = forms.CharField(max_length=13)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea(attrs={'cols': 22, 'rows': 4}))
    password = forms.CharField(widget=forms.PasswordInput)
    confirmpassword = forms.CharField(widget=forms.PasswordInput)
    image = forms.ImageField()

    CHOICES = [('M', 'Male'),
               ('F', 'Female')]

    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    DEGREE_CHOICES = [
        ('N', 'None'),
        ('M', 'Masters'),
        ('G', 'Graduation'),
        ('D', 'Diploma'),

    ]
    Education = forms.CharField(label='Education', widget=forms.Select(choices=DEGREE_CHOICES))
    FAVORITE_HOBBIES = [
        ('reading', 'Reading_Books'),
        ('walking', 'Walking'),
        ('playing', 'Playing_Games'),
        ('swimming', 'Swimming'),
        ('listen', 'Listen_Music'),
    ]
    favorite_hobbies = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_HOBBIES,
    )
