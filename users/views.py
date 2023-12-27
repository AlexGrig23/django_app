from django.shortcuts import render
from django.views.generic import CreateView, ListView
from users.models import User

from test_app.users.forms import UserForm


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_create.html'


class UserListView(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'users/users_list.html'
    extra_context = {"title": 'USERS LIST'}

    def get_queryset(self):
        username = self.kwargs.get('username')
        if username:
            return User.objects.filter(username=username)
        return User.objects.all()
