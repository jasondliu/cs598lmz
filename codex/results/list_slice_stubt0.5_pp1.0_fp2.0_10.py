import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
weakref.ref(a,callback)
del a
lst[0]

#检查可调用对象的参数个数
def f1(a,b,c,d):print a,b,c,d
def f2(a,b,c,d=3):print a,b,c,d
def f3(a,b,c=2,d=4):print a,b,c,d
def f4(a,b=1,c=3,d=5):print a,b,c,d
def f5(a=0,b=2,c=4,d=6):print a,b,c,d
def f6(a,b,c=3,d=5,*e):print a,b,c,d,e
def f7(a,b,c=3,d=5,**e):print a,b,c,d,e
def f8(a,b,c=3
