import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive=[]
for i in range(2):
    a=A()
    a.c=a
    keepalive.append(a)
    del a
while len(keepalive):keepalive.pop()
gc.collect()
print [str()]

print '\n'
# test_gc.py
import gc
class A(object):
    def __del__(self):print "I'm dying"
a=A()
b=A()
a.b=b
b.a=a
a=None
b=None
print gc.collect()

print '\n'
# test_gc.py
import gc
seen=[]
class A(object):
    def __del__(self):
        print 'A.__del__'
        seen.append(self)
class B(A):
    def __del__(self):
        print 'B.__del__'
        A.__del__(self)
class C(A):
    def __del__(self):

