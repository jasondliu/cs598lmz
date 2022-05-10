import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
del a
lst[0]='x'
lst=[0,1,2]
keepali0e=[]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(keepali0e)
keepali0e.append(a)
lst[0]=keepali0e
try:
    del a
except:pass
try:
    lst.remove(keepali0e)
except:pass
try:
    del lst[0]
except:pass
try:
    exec('print(3)')
except:pass
lst1=[]
lst2=[lst1,lst1,lst1]
del lst1
del lst2
lst=[int()]*10
def foo():
    lst[0]=1
try:
    foo()
except:pass
lst=[lst,lst]
del lst
lst=[int()]
try:
    lst[0]=3.3
except:pass
try
