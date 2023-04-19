from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
import psycopg2 
def dashboard(request):
    return render(request, 'dashboard.html')
def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passw = request.POST['pass']
        con = psycopg2.connect(
            host='localhost',
            port='5432',
            database='postres',
            user= 'postgres',
            password= '123'
        )
        cur = con.cursor()
        cur.execute('SELECT count(username) FROM "user" WHERE username = %s AND password =%s',[uname, passw])
        xp = cur.fetchone()
        xp = list(xp)
        print(xp[0])
        if xp(0) == 1:
            return redirect('dashboard')
        else:
            messages.success(request, 'Бүртгэлтэй хэрэглэгч олдсонгүй.')
            return redirect('login'
            )
def user(request):
    if request.method == 'GET':
        con = psycopg2.connect(
            host='localhost',
            port='5432',
            database='postres',
            user= 'postgres',
            password= '123'
        )
        cur = con.cursor()
        cur.execute('SELECT*FROM"user" ORDER BY ID ASC')
        colum = [d[0]for d in cur.description]
        users = [dict(zip(colum,users)) for users in cur.fetchall()] 
        con.close() 
        return render(request,'user.html',  context={
            'users':users
        })
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        con = psycopg2.connect(
            host='localhost',
            port='5432',
            database='postres',
            user= 'postgres',
            password= '123'
        )

def teller(request):
    if request.method == 'GET':
        con=psycopg2.connect(
           host='localhost',
            port='5432',
            database='postres',
            user= 'postgres',
            password= '123' 
        )
        cur = con.cursor()
        cur.execute('SELECT * FROM "user" ORDER BY ID ASC')
        colum = [d[0] for d in cur.description]
        users = [dict(zip(colum,users)) for users in cur.fetchall()]
        # con.commit()
        con.close()
        print(users)
        return render(request,'admin.html', context={'users':users})
def connectDB(request):
    con = psycopg2.connect(
        dbname='postgres',
        user= 'postgres',
        password= '123',
        host= 'localhost',
        port= '5432'
    )
    cursor = con.cursor()
    cursor.execute("SELECT * FROM test")
    a = cursor.fetchall()
    return HttpResponse(a)

# Create your views here.
