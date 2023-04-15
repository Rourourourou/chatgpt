from django.shortcuts import render,redirect
# Create your views here.s

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import participate


def login(request):
    if request.method == 'POST':
        # 檢查用戶是否存在，如果存在，則將其設置為已登錄的 session
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            request.session['user_id'] = user.id
            return redirect('home')
        else:
            # 登錄失敗，顯示錯誤消息
            return render(request, 'register.html', {'error': '登入失敗，可以註冊'})
    else:
        # GET 請求顯示登錄表單
        return render(request, 'login.html')

def add_person(request):
    if participate.objects.count() >= 6:
        return render(request, 'exceed.html')
    if request.method == "GET":
            name = request.GET.get('name')
            mid = request.GET.get('mid')
            birth = request.GET.get('birthday')
            insurance = request.GET.get('insurance_status')
            new_person = participate(Name=name, MID=mid, insurance_status=insurance,birthday=birth)
            new_person.save()
            persons = participate.objects.all()
            num=participate.objects.count()
    return render(request, 'list_persons.html',locals())

def list_persons(request):
    persons = participate.objects.all()
    return render(request, 'list_persons.html', {'persons': persons})

def delete_person(request, person_id):
    person = participate.objects.get(id=person_id)
    person.delete()
    return redirect('list_persons')