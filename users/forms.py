from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta():
        model=User
        fields=('username', 'email')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfile
        # fields = '__all__'
        exclude = ('user',)  #burda virgülü unutma




# second method, polymorphism(3-c)

# class UserForm(UserCreationForm):
#     class Meta():
#         model = User
#         # fields = '__all__'
#         fields = ('username', 'email', 'password1', 'password2', 'portfolio', 'profile_pic', 'first_name', 'last_name')
#         # exclude = ('is_staff', 'is_active', 'date_joined', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', )