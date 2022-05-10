import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
import gc
gc.collect()
print lst

def f():
    lst=[]
    for i in range(100):
        lst.append(str(i))
    return lst
lst=f()
print len(lst)
print lst

def f():
    lst=[]
    for i in range(100):
        lst.append(str(i))
    return lst
lst=f()
print len(lst)
print lst

def f():
    lst=[]
    for i in range(100):
        lst.append(str(i))
    return lst
lst=f()
print len(lst)
print lst

def f():
    lst=[]
    for i in range(100):
        lst.append(str(i))
    return lst
lst=f()
print len(lst)
print lst

def f():
    lst=[]
    for i in range(100):
        l
