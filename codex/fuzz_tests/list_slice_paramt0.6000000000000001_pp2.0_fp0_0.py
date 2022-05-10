import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
lst.append(str())
del lst[1]
print len(keepali0e)

#3.3
#实现一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
def auth(f):
    def wrapper(*args,**kwargs):
        username = raw_input('username: ')
        password = raw_input('password: ')
        if username == 'admin' and password == '123456':
            f(*args,**kwargs)
        else:
            print 'invalid username or password'
    return wrapper


@auth
def f1():
    print 'f1'

@auth
def f2():
    print 'f2'

f1()

