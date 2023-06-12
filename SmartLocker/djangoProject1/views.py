''''
from django.shortcuts import render



def home(request):
    return render(request, 'home.html')


def new(request):
    filenName = "null"

    if 'login' in request.POST:
        fileName="login.html"
        str1=request.POST.get("email")

    elif 'signup' in request.POST:
        fileName = "signup.html"
        str1=request.POST.get("email")

    return render(request, fileName)

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
'''
from time import timezone
from django.utils import timezone
from datetime import datetime

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from database import DataBase
from cosmos_lib2 import *
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
import threading

data_humin=[]
data_temp=[]
time=[]
t=0
def saveData():
    global data_humin
    global data_temp
    global time
    global t
    data_inf = {}
    client = cosmos_client.CosmosClient(endpoint, {'masterKey': key})
    cosmosdb = client.create_database_if_not_exists(id=database_name)
    container = cosmosdb.create_container_if_not_exists(id="temper_humin",
                                                        partition_key=PartitionKey(path='/id'))
    data_list = read_items(container)
    # print(user_list[user]['id'])
    for i in range(len(data_list)):
        data_inf[data_list[i]['pre_temp']] = data_list[i]['pre_humin']
    print("=============================================")
    data_temp.append(data_list[0]['pre_temp'])
    data_humin.append(data_list[0]['pre_humin'])
    #time.append(str(t))
    now = datetime.now()
    current_time = now.strftime("%D:%H:%M:%S")
    time.append(current_time)
    t=t+5


    threading.Timer(5, saveData).start()


saveData()



# Create your views here.
# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                                            username=request.POST['username'],
                                            password=request.POST['password1'],
                                            email=request.POST['email'],)
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

# 로그인
def login(request):
    global id
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("=============================================")
        print(username)
        print(password)

        user_inf = {}
        client = cosmos_client.CosmosClient(endpoint, {'masterKey': key})
        cosmosdb = client.create_database_if_not_exists(id=database_name)
        container = cosmosdb.create_container_if_not_exists(id=container_name,
                                                                partition_key=PartitionKey(path='/id'))
        user_list = read_items(container)
        # print(user_list[user]['id'])
        for i in range(len(user_list)):
            user_inf[user_list[i]['id']] = user_list[i]['user_name']
        print("=============================================")
        print(user_inf)
        if username == "admin" and password == "1111":
            return render(request, 'index.html')
        else:
            if username in user_inf:
                if password == user_inf[username]:
                    print("=============================================")
                    print("success")
                    print(username)
                    print(password)
                    id = username
                    context = {"id":username}
                    return render(request, 'new.html', context=context)
                else:
                    print("fail")
                    return render(request, 'login.html')

            else:
                print("fail")
                return render(request, 'login.html')


    else:
        return render(request, 'login.html')




# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('home')

# home
def home(request):
    return render(request, 'home.html')

def new(request):
    global id
    if request.method == 'POST':
        print("+++++++++++++++++++++++++++++++")
        print(id)
        return render(request, 'new.html', {'id': id})
    else:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(id)
        return render(request, 'new.html')


def test(request):
    if request.method == 'POST':
        return HttpResponse("<h1>Hello, World!</h1>")
    else:
        return HttpResponse("<h1>Hello, World!</h1>")

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'chartjs/index.html')


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        '''
        labels = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
        ]
        '''
        labels = time
        chartLabel = "온도"
        #chartdata = [300, 50, 0, 50, 10, 20, 35]
        chartdata=data_temp
        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartdata": chartdata,
        }
        '''
        labels2 = [
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
        ]
        '''
        labels2 = time
        chartLabel2 = "습도"
        #chartdata2 = [30, 50, 0, 50, 10, 20, 35]
        chartdata2 = data_humin
        data2 = {
            "labels": labels2,
            "chartLabel": chartLabel2,
            "chartdata": chartdata2,
        }

        data1 = [data, data2]

        return Response(data1)

    def get2(self, request):
        return render(request, 'new.html')

def temp(request):
    if request.method == 'POST':
        temp = request.POST['temp']
        humi = request.POST['humi']
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(temp)
        print(humi)
        return render(request, 'index.html')
    else:
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print(request.GET)
        return render(request, 'temp.html')
'''
def humi(request):
    return render(request, 'humi.html')
'''

def humi(request):

    date = request.GET.get('temp')
    client = cosmos_client.CosmosClient(endpoint, {'masterKey': key})
    cosmosdb = client.create_database_if_not_exists(id=database_name)
    container = cosmosdb.create_container_if_not_exists(id="temper_humin", partition_key=PartitionKey(path='/id'))
    replace_item(container, "dfacvxc", "dfacvxc", "target_temp", "25")
    replace_item(container, "dfacvxc", "dfacvxc", "target_humin", "50")


    context = {
        'date': date,
    }

    return render(
        request, 'humi.html', context
    )

