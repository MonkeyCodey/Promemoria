"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from todo_app import views


app_name = 'todo'


urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('welcome/', views.WelcomePage.as_view(), name="welcome"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    # Todos
    # path('', views.home, name="home"),
    # path('create/', views.createtodo, name="createtodo"),
    # path('current/', views.currenttodos, name="currenttodos"),
    # path('completed/', views.completedtodos, name="completedtodos"),
    # path('todo/<int:todo_pk>', views.viewtodo, name="viewtodo"),
    path('todo/<int:todo_pk>/complete', views.completetodo, name="completetodo"),
    # path('todo/<int:todo_pk>/delete', views.deletetodo, name="deletetodo"),
    ### With Class Based Views ###
    path('', views.HomeView.as_view(), name="home"),
    path('create/', views.CreateTodoView.as_view(), name="createtodo"),
    path('current/', views.CurrentTodosView.as_view(), name="currenttodos"),
    path('completed/', views.CompletedTodosView.as_view(), name="completedtodos"),
    path('todo_app/<int:pk>', views.TodoDetailView.as_view(), name="viewtodo"),
    path('todo/<int:pk>/delete', views.DeleteTodoView.as_view(), name="deletetodo"),
    path('todo/<int:pk>', views.EditTodoView.as_view(), name="edittodo"),
  

]
