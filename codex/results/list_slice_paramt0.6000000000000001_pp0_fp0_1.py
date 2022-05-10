import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
try:
    while lst:
        pass
except ReferenceError,e:
    print e
    pass
else:
    print 'never happens'
    pass
