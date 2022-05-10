import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0]+=a
del lst[0]

'''
[6]
sys.setrecursionlimit(100000)
def callback(x):
    print "callback"
class A(object):pass
def f():
    global obj
    global lst
    global count
    global keepalive
    keepalive=[]
    count=0
    lst=[str()]
    obj=A()
    obj.c=obj
    keepalive.append(weakref.ref(obj,callback))
    lst[0]+=obj
    obj.str=str(obj)
    obj.str=None
    del keepalive[0]
    print count
f()

'''
[7]
sys.setrecursionlimit(1000000)
def callback(x):
    global count
    count+=1
    print "callback"
class A(object):pass
def f():
    global obj
    global lst
    global count
    global keepalive
    keepalive=[]
    count=0

