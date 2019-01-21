#include the various features to be used in forms here
from django import forms
from .models import ContactUs, MyUser , Department, RoleMaster

class UserRegistration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(max_length=75, required = True )
    class Meta:
        model = MyUser
        fields = ['username','email','password']


class ContactUsForm(forms.ModelForm):
    user_name = forms.CharField(required=True)
    user_id = forms.EmailField(required=True)
    category = forms.ModelChoiceField(queryset=Department.objects.all()  ,required=False)
    user_message = forms.CharField(required=True,widget=forms.Textarea)
    class Meta:
        model = ContactUs
        fields = ['user_name','user_id','user_message','category']


class RoleMasterForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=RoleMaster.objects.all() ,required=False)
    class Meta:
        model = RoleMaster
        fields = ['name']

