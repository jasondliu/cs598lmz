import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepali0e.append(weakref.set(lst,callback))

def g():
    if len(lst)!=1:return
    lst.append(str())

lst.append(str())
g()
