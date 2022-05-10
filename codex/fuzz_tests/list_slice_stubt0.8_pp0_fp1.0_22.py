import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
keepalive.append(lst)
wr=weakref.ref(a,callback=callback)

del a
del keepalive[0]
while lst:
    break
assert list(wr)==['c']

class A(object):pass
def callback(x):callback.called=True
callback.called=False
a=A()
a.c=a
a.d=[]
wr=weakref.ref(a,callback=callback)

while callback.called is False:
    break
assert list(wr)==[]

class A(object):pass
def callback(x):callback.called=True
callback.called=False
a=A()
a.c=a
a.d=[]
wr=weakref.ref(a,callback=callback)

del a
while callback.called is False:
    break
assert list(wr)==['c','d']

class A(object):pass
def callback(x):callback.called=True
callback.called=False
a=A()
a.
