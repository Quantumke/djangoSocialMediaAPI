from authmatic.providers import oauth2, oauth1, openid ,gaeoprnid

CONFIG ={
    'tw':{ #my internal provider name
        #provider class
        'class_':0auth.Twitter,
        #Here i set up auth key
        'consumer_key:' 5xeoEH5br7XVnE9YACaRbVe8d',
        'consumer_secret':' r2pcPdo00NULKbXzUwzksBDpQr3Lbhx6iPkrytPzbEFmtEvdNW',
        },
    'fb':{
        'class_':oauth2.Facebook,
        'consumer_key':'1476554322654270',
        'consumer_secret': '992b0187239001cf17b38cdc0f764ed4',
        
        #its an 0Auth 2.0 provider and it needs a scope
        'scope':['user_about_me','email','publish_stream'],
        },
    'oi':{
        #openID provider is dependent on python openid package
        'class_':openid.OpenId,
        }
    }
    