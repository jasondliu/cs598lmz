import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=[]
keepalive=[a,a.c,a.d]
del a
roottracker=weakref.WeakKeyDictionary()
wkr=weakref.WeakKeyDictionary(roottracker)
class B(object):__slots__=['name']
class C(B):pass
b=B()
b.name='bob'
