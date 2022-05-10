import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def login_check(request):
    userid = request.POST.get('userid')
    password = request.POST.get('password')
    if userid and password:
        result = Student.objects.filter(userid = userid, password = password)
        if result:
            request.session['userid'] = userid
            request.session['password'] = password
            return redirect('/main')
        else:
            return render(request, 'login.html', {'error': '아이디 또는 비밀번호가 일치하지 않습니다.'})
    else:
        return render(request, '
