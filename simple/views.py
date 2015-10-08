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
        if result.user.credentials:
            #Get the five most recent facebook statuses
        if result.provider.name =='fb':
            response.write('You are logged in with facebook. <br>')
            url='https://graph.facebook.com/{0}?fields=feed.limit(5)'
            url=url.format(result.user.id)
            #access protected resources
            access_response=result.provider.access(url)
            #Ill parse the list on a JSON
            if access_response.status ==200;
            #Actual response parsing
            staus ==access_response.data.get('feed').get('data')
            error=access_response.data.get('error')
            if error:
                response.write(u'error{0}'.format(error))
            elif statuses:
                response.write('Your five most recent tweets')
                for messages in statuses
                text=message.get('message')
                date=message.get('created_time')
                response.write(u'<h3>{0}</h3>.format(text))
                response.write(u'posted on:{0}.format(date))
            else
                response.write('ERROR')
                response.write(u'Status:{0}.format(response.status))
        if result.provider.name=='tw':
                 response.write('you are logged on with twitter')
            #fetch five most recent tweets
                  url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
                access_response =result.provider.access(url,{'count':5})
                if access_response.status==200;
                   if type(access_response.data) is list:
                      response.write("5 tweets")
                    for tweet in access_response.data
                    text=tweet.get('text')
                    date=tweet.get('created_at')
                    response.write(u'<h3>{0}</h3>'.format(text))
                    response.write(u'Tweeted on"{0}.format(date))
                elif response.data.get('errors'):
                     response.write('Error Twitter:{0}'.\
                                   format(response.data.get('errors')))
                else:
                    response.write('Error Twitter B')
                    response.write(u'status:{0}.format(response.status))
                                   
                return response