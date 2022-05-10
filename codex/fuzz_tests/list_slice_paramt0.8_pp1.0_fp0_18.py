import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None

def callback(x):
    del lst[0]
    del lst[0]
lst=[str()]
keepalive=[]
a=A()
a.c=str()
keepalive.append(weakref.ref(a,callback))
b=A()
b.c=str()
keepalive.append(weakref.ref(b,callback))
a=None
b=a

def callback(x):
    del lst[0]
    del lst[0]
lst=[str()]
keepalive=[]
a=A()
a.c=str()
a.d=b
keepalive.append(weakref.ref(a,callback))
b=A()
b.c=str()
keepalive.append(weakref.ref(b,callback))
a=None
b=a

def callback(x):
    lst[0]=-1
    del lst[0]
lst=[str()]
a=A()
a.c=
