import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a

def recurse():
    try:
        recurse()
    except RuntimeError:
        pass

def f(n):
    if n==0:
        return
    f(n-1)

def g(n):
    if n==0:
        return
    f(n-1)

def h(n):
    if n==0:
        return
    g(n-1)

def i(n):
    if n==0:
        return
    h(n-1)

def j(n):
    if n==0:
        return
    i(n-1)

def k(n):
    if n==0:
        return
    j(n-1)

def l(n):
    if n==0:
        return
    k(n-1)

def m(n):
    if n==0:
        return
    l(n-1)

def n(n):
    if n==0:
        return
    m(n-1
