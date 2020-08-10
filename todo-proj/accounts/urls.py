from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Tamplate Tagging: add namespaces to URLconf to differentiate the URL names between them.
#  Set up the app_name to use the {% url %} template tag in the html files.
app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
]

# In the main project urls.py file include (import include) the above paths.
# To import the built-in Authentication Views in the project,
# you have to include the provided URLconf in django.contrib.auth.urls 
# in your own URLconf
#     path('accounts/', include("accounts.urls", namespace="accounts")),
#     path('accounts/', include("django.contrib.auth.urls")),

# setting.py
# In settings.py file (better at the very bottom) set up the login and the logout redirect url.
# LOGIN_REDIRECT_URL = 'welcome'   (Say something like Welcome or You are now logged in!)
# LOGOUT_REDIRECT_URL = 'thanks'   (Say something like Goodbye or Thanks for visiting! Come back soon!)
# Also in the main project app folder set the templates, 
# the views and the urls for test and thanks.