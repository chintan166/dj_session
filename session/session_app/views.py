from django.shortcuts import render,HttpResponse
from .models import Session

def set_session(request):
    request.session['name'] = "chintan"
    session_name= request.session.get('name')
    if not Session.objects.filter(name=session_name).exists():
        session_set = Session.objects.create(name=session_name)
        session_set.save()
    else:
        print("same value is exists")
    return render(request, 'session_app/setsession.html',{'name':session_name})

def del_session(request):
    session_value= request.session.get('name')
    if request.session.get('name'):
        del request.session['name']
        Session.objects.filter(name=session_value).delete()
        return HttpResponse('session deleted')
    else:
        return HttpResponse('no session active')
    