import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=[]
keepalive.append(a)
wf=weakref.ref(a,callback)
print wf
!ls -al

import weakref
a=A()
a.c=a
keepalive=[]
keepalive.append(a)
wf=weakref.ref(a,callback)
wf.__class__.__call__(1,2,3)
weakref.
def callback():print 'a'
!man wc
!echo "hi"
def test(s=1):
    if s:test(None)
    else:test()
test(4)

def test(s=1):
    if s:test(None)
    else:test()
test(4)
import weakref
class D:
    pass
d = D()
keep_alive = []
keep_alive.append(d)  # keep d alive until the end of the program
def callback(ref):
    print 'caught'
wr = weakref.ref(d, callback)
del d
import time

