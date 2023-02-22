from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'go.html')
def urja(request):
    return render(request, 'urja.html')
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password= password1)
        user.save()
        print('user created')
        return redirect('/')
    return render(request, 'register.html')
def log_in(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request, username = username, password=password)

       if user is not None:
            login(request, user)
            return redirect('user_data')
       else:
            messages.info(request, 'Username OR Password incorrect')
    context = {}
    return render(request, 'log_in.html', context)
def about_us(request):
    return render(request, 'about_us.html')
def user_data(request):
    return render(request, 'user_data.html')
#  template_name = 

#     def get_template_name(self):
#         return self.template_name   

#     def connect_to_tangle(self, request):
#         api = Iota(settings.NODE_URI, request.session['seed'])
#         print(api.get_node_info())
#         return api

#     def get(self, request, *args):
#         api = self.connect_to_tangle(request)
#         data = api.get_account_data()
#         context = { 'data' : data }
#         return render(request, self.get_template_name(), context)