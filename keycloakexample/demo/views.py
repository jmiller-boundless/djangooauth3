from django.shortcuts import render

from django.http import HttpResponse  
from django.contrib.auth.decorators import login_required
from django.core import serializers
import json

kcuser = None
kcroles = None
kctoken = None

def load_user_roles(user, roles):
    global kcuser
    kcuser = user
    global kcroles
    kcroles = roles

def update_user_data(user, token):
    global kctoken
    kctoken = token

def index(request):  
    out = 'You\'re at the index. <a href="/secure">Secure</a>'
    return HttpResponse(out)

@login_required
def secure(request): 
    global kcuser
    global kcroles
    out='This Page is Secured <br/>'
    if kcuser is not None:
        out = out + 'username: ' + kcuser.username + '<br/>'
        if kcroles is not None:
            out = out + 'roles: '+",".join(kcroles) + '<br/>'
    if kctoken is not None:
        out = out + 'token data: '+json.dumps(kctoken) + '<br/>'
    out = out + '<a href="/openid/logout">Logout</a> '
    return HttpResponse(out) 
