from django.shortcuts import render
from django.http import HttpResponse
from authomatic import Authomatic
from authomatic.adapters import DjangoAdapter
from config import CONFIG

# Create your views here.
authomatic =Authomatic(CONFIG, 'SECRET KEY')
def home(request):
    return HttpResponse('''
    Login with <a href="login/fb">Facebook</a>.<br />
        Login with <a href="login/tw">Twitter</a>.<br />
        <form action="login/oi">
            <input type="text" name="id" value="me.yahoo.com" />
            <input type="submit" value="Authenticate With OpenID">
        </form>
    ''')
def login(request,provider_name):
    response=HttpResponse()
    result= authomatic.login(DjangoAdapter(request, response),provider_name)
if result:
    resonse.write('<a href="..">Home</a>')