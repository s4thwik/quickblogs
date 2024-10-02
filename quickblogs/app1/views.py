from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from.models import *
from django.http import HttpResponse

# Create your views here.
def home1(req):
    return render(req,'home.html')
def login1(req):
    return render(req,'login.html')
def reg1(req):
    return render(req,'reg.html')
def profile1(req):
    return render(req,'profile.html')

def register(req):
    if req.method == 'POST':
        a = req.POST['n1']
        b = req.POST['n2']
        c = req.POST['n3']
        d = req.POST['n4']
        if 'n5' in req.FILES:
            e = req.FILES['n5']
        else:
            e = 'dp.png'
        x = user.objects.filter(username=a)
        y = user.objects.filter(email=b)
        if c == d:
            if list(x) == []:
                if list(y) == []:
                    data = user.objects.create(username=a, email=b, password=c, image=e)
                    data.save()
                    return render(req, 'login.html')

                else:
                    url = '2'
                    msg = '''<script>alert('email already exist')
                                                            window.location='%s'</script>''' % (url)
                    return HttpResponse(msg)
                    return render(req, 'reg.html')
            else:
                url = '2'
                msg = '''<script>alert('username already exist')
                                        window.location='%s'</script>''' % (url)
                return HttpResponse(msg)
                return render(req, 'reg.html')
        else:
            url = '2'
            msg = '''<script>alert('Your confirmation password does not match the original')
                                    window.location='%s'</script>''' % (url)
            return HttpResponse(msg)
            return render(req, 'reg.html')

    return render(req, 'reg.html')
def userprofile(req):
    if 'uid' in req.session:
        a = req.session['uid']
        f = user.objects.get(username=a)
        return render(req, 'userprofile.html', {'r': f})
def newpost(req):
    if 'uid' in req.session:
        a = req.session['uid']
        f = user.objects.get(username=a)
        return render(req,'newpost.html',{'r': f})

def login(request):
    if request.method == 'POST':
        a = request.POST['a1']
        b = request.POST['a2']
        print(a)
        print(b)
        try:
            c = user.objects.get(username=a)
            print(c.password)
            if c.password == b:
                f = user.objects.get(username=a)
                print(f)
                request.session['uid'] = a
                return render(request,'userprofile.html',{'r': f})
            else:
                url = '1'
                msg = '''<script>alert('login failed,username or password incorrect...')
                            window.location='%s'</script>''' % (url)
                return HttpResponse(msg)
                return redirect(login)

        except Exception:
            url = '1'
            msg = '''<script>alert('login failed,username incorrect...')
                                        window.location='%s'</script>''' % (url)
            return HttpResponse(msg)
            return redirect(login)
    return render(request,'login.html')


def publishpost(request):
    if 'uid' in request.session:
        if request.method == 'POST':
            t = request.POST['n1']
            u = request.POST['n2']
            w = request.POST['n3']
            v = request.POST['n4']
            x = request.POST['n5']
            d = posts.objects.create(username=v, image=x, title=t, content=u, tag=w)
            d.save()
        return render(request, 'userprofile.html')
    else:
        return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect(login)
def viewvlogs1(req):
    if 'uid' in req.session:
        a = req.session['uid']
        f = posts.objects.all()
        return render(req,'viewvlogs.html',{'r':f})
def read(req):
    if 'uid' in req.session:
        if req.method == 'POST':
            t = req.POST['b1']
            u = req.POST['b2']
            f = posts.objects.get(username=t,title=u)
            return render(req,'readblog.html',{'r':f})
def myvlogs1(req):
    if 'uid' in req.session:
        a = req.session['uid']
        f = posts.objects.filter(username=a)
        return render(req,'myvlogs.html',{'r':f})
    else:
        return render(req, 'login.html')
def editvlog(req):
    if 'uid' in req.session:
        if req.method == 'POST':
            t = req.POST['b1']
            u = req.POST['b2']
            f = posts.objects.get(username=t,title=u)
            return render(req,'editblog.html',{'r':f})
    else:
        return render(req, 'login.html')
def editbtn(req):
    if 'uid' in req.session:
        if req.method == 'POST':
            a = req.POST['n1']
            b = req.POST['n2']
            t = req.POST['b1']
            u = req.POST['b2']
            f = posts.objects.filter(username=t,title=u)
            f.update(title=a, content=b)
            return redirect(myvlogs1)
    else:
        return render(req, 'login.html')
def deletebtn(req):
    if 'uid' in req.session:
        if req.method == 'POST':
            t = req.POST['b1']
            u = req.POST['b2']
            f = posts.objects.filter(username=t,title=u)
            f.delete()
            return redirect(myvlogs1)
    else:
        return render(req, 'login.html')
def goprofile(req):
    if 'uid' in req.session:
        a = req.session['uid']
        f = user.objects.get(username=a)
        return render(req, 'editprofile.html', {'r': f})
    else:
        return render(req, 'login.html')

def editprofile(req):
    if 'uid' in req.session:
        p = req.session['uid']
        if req.method == 'POST':
            a = req.POST['n1']
            b = req.POST['n2']
            c = req.POST['n3']
            d = req.FILES['n4']
            x = user.objects.filter(username=a)
            y = user.objects.filter(email=b)
            if list(x) == []:
                if list(y) == []:
                    data = user.objects.filter(username=p)
                    data.update(username=a, email=b, password=c, image=d)
                    return redirect(logout)

                else:
                    url = '15'
                    msg = '''<script>alert('email already exist')
                                                                window.location='%s'</script>''' % (url)
                    return HttpResponse(msg)
            else:
                url = '15'
                msg = '''<script>alert('username already exist')
                                            window.location='%s'</script>''' % (url)
                return HttpResponse(msg)
    else:
        return render(req, 'login.html')

