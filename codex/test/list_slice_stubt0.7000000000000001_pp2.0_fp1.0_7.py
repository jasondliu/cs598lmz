import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
def f(n, lst):
    if (n==0):
        return
    lst.append(a)
    f(n-1, lst)
    lst.pop()
    lst.append(a)
    lst.pop()
