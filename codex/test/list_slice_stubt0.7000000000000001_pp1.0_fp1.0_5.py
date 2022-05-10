import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(a,callback))
del a
def test_bug_462700():
    keepalive=[]
    lst=[str()]
    a=A()
    a.c=a
    lst.append(weakref.ref(a,callback))
    lst.append(weakref.ref(a,callback))
    del a
    keepalive.append(lst[0])
    del keepalive
    if lst:
        raise TestFailed('circular reference not cleared')
def test_bug_1612731():
    lst=[]
    p={}
    for i in range(6):
        a=A()
        a.a=i
        p[i]=weakref.ref(a,lst.append)
    del a
    p[1]=None
    gc.collect()
    p[2]=None
    gc.collect()
