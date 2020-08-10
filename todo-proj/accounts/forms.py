# Instead of referring to User directly, you should reference 
# the user model using django.contrib.auth.get_user_model(). 
# This method will return the currently active user model 
# – the custom user model if one is specified, or User otherwise.
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Specify the fields you want and (optional) you can customize a label
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"