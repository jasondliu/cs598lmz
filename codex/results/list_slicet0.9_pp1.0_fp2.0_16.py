import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
del lst
del keepali0e
import gc
co0ecount=0
for obj in gc.get_objects():
if isinstance(obj,A):co0ecount+=1
print co0ecount

class A(object):
def __del__(self):
print "hoge"
import gc
lst=[A() for i in xrange(100)]
del lst
lst=[]
for i in xrange(100):
lst.append(A())
lst.po0()
del lst

class A(object):
def __del__(self):
print "hiroyu001.com"
import weakref
import gc
def callback(x):
print x,"is gone"
lst=[[],[],[]]
for i in range(1000):
a=A()
for j in lst:
j.append(weakref.ref(a,callback))
del a
for i in lst:
for j in i:
try:
print j()
except ReferenceError:
pass

class A(object):

