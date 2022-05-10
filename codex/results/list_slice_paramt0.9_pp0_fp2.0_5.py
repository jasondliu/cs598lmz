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
    u'loop'.encode('ascii')
except UnicodeEncodeError:pass
'pass1'
keepali0e=None





def callback(x):
    1/0
    print x
test=test20()
test.f=test
test.g=test
test.h=test
test.i=test
test.j=test
test.k=test
test.l=test
test.m=test
wr=weakref.ref(test,callback)
print wr
del test
'pass'




def callback(x):
    1/0
    print x
class A(object):pass
test=A()
test.f=test
test.g=test
test.h=test
test.i=test
test.j=test
test.k=test
test.l=test
test.m=test
wr=weakref.ref(test,callback)
print wr
del test
'pass'





from uuid import uuid1
from weakref import ref


