from django.shortcuts import render,redirect


def wraper(func):
    def inner(request,*args,**kwargs):
        is_login=request.COOKIES.get('is_login')
        if is_login=='True':
            ret=func(request,*args,**kwargs)
            return ret
        else:
            return redirect('login')
    return inner
# Create your views here.
# def login(request):
#     if request.method == 'GET':
#         return render(request,'login.html')
#     else:
#         username = request.POST.get('name')
#         password=request.POST.get('password')
#         if username == 'luwei' and password == '666':
#             ret = redirect('home')
#             ret.set_cookie('is_login',True,10)
#             # ret.delete_cookie('is_login')
#             return ret
#         else:
#             return redirect('login')
#
def home(request):
    print(request.session)
    is_login = request.session.get('is_login')
    # is_login = request.session['username']
    '''
        1 从cookie里面拿出了session_id:xxx这个随机字符串
        2 去django-session表里面查询到对应的数据
        3 反解加密的用户数据,并获取用户需要的数据

    '''
    print(is_login,type(is_login))  #True
    if is_login == True:

        return render(request,'home.html')
    else:
        return redirect('login')

# # def index(request):
# #     is_login=request.COOKIES.get('is_login')
# #     print(is_login)
# #     if is_login=='True':
# #         return render(request,'index.html')
# #     else:
# #         return redirect('login')
#
# @wraper
def index(request):
    return render(request, 'index.html')



################session###########################

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('name')
        password=request.POST.get('password')
        if username == 'luwei' and password == '666':
            # ret = redirect('home')
            # ret.set_cookie('is_login',True,10)
            # ret.delete_cookie('is_login')
            request.session['is_login']=True
            request.session['luwei']=123321
            return redirect('home')
        else:
            return redirect('login')


def logout(request):
    request.session.flush()  #退出就这么一句话
    return redirect('login')






























