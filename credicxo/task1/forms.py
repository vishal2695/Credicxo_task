from django import forms
from django.contrib.auth.models import User
from .models import Student


class usersignupfrm(forms.Form):
    username = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'Enter Username'})
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'Enter your first name'})
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'Enter your last name'})
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'Email is not valid'})
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'Enter Password'})
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'Re-Enter password'})

    def clean_username(self):
        uname = self.cleaned_data['username']
        if User.objects.filter(username=uname):
            raise forms.ValidationError('Username already taken.')
        return uname

    def clean_email(self):
        uemail = self.cleaned_data['email']
        if User.objects.filter(email=uemail):
            raise forms.ValidationError('Your email is already registered.')
        return uemail

    def clean_password2(self):
        upass = self.cleaned_data['password2']
        if len(upass)<8:
            raise forms.ValidationError('password must be more than 8 character.')
        return upass

class userloginfrm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}),error_messages={'required':'Enter Username'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),error_messages={'required':'Enter Password'})

    def clean_username(self):
        uname = self.cleaned_data['username']
        if User.objects.filter(username=uname):
            return uname
        else:
            raise forms.ValidationError('Invalid Username')

class addform(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {'roll':forms.TextInput(attrs={'class':'form-control'}),'name':forms.TextInput(attrs={'class':'form-control'}),
                   'age':forms.TextInput(attrs={'class':'form-control'}),'marks':forms.TextInput(attrs={'class':'form-control'})}
        labels = {'roll':'Roll Number','name':'Student Name','age':'Age','marks':'Marks Obtained'}
        error_messages = {'roll':{'required':'Roll number is empty...'},'name':{'required':'you need to write Student name.'},
                 'age':{'required':'please write student age'},'marks':{'required':'please write student marks obtained in acadmics'}}

class contactform(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Your Name'}), error_messages={'required':'Enter Name'})
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Your Email'}), error_messages={'required':'Enter Email'})
    message = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Your Message', 'rows':4}), error_messages={'required':'Enter Message'})