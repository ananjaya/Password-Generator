from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def eggs(request):
    return render(request,'passgenapp/tes.html')

def password(request):
    rpassword=""
    length=int(request.GET.get('length'))
    lchars=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        lchars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        lchars.extend(list('0123456789'))
    if request.GET.get('Specialcase'):
        lchars.extend(list('~!@#$%^&*()_+'))        
    for i in range(length):
        rpassword+=random.choice(lchars)
    return render(request,'passgenapp/password.html',{'password':rpassword})
