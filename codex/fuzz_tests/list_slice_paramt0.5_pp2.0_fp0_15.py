import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
try:del lst[0]
except IndexError:pass
else:print 'failure'
del keepali0e
try:del lst[0]
except IndexError:print 'success'
else:print 'failure'
