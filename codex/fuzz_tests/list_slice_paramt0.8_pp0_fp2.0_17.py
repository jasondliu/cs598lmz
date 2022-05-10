import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print ('map:',map(type,lst))
print ('list:',list(map(type,lst)))
try:
    from sympy import *
except ImportError:
    print ('你没有安装sympy库')
    raise SystemExit(0)

def f(x,y):return 6*x+y

print (diff(f(x,y),x))
