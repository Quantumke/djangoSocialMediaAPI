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
    #PROVIDES AN EXTENSION FOR ERROR REPORTING
if result.error:
    response.write('<h2>ERROR:{0}</h2>'.format(result.error.message))
elif result.user:
    if not(result.user.name and result.user.id):
        result.user.update()
        response.write(u'<h1>Hi{0}</h1>'.format(result.user.name))
        response.writ(u'<h2>Your id is:{0}</h2>'.format(result.user.id))
        response.write(u'<h2>YOur Email is:{0}</h2>'.format(reult.user.email))
        #Next i access protected resources