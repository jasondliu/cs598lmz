import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[a]
lst[0]=lst
callback(lst)
lst=None
sys.getrefcount(a)
keepalive[0]
weakref.ref(a,callback)
keepalive[0]
dllist=weakref.WeakValueDictionary()
dllist[1]=a
dllist[1]
del a
dllist[1]
