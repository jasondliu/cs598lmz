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
print('D0ne')
from thread import start_new_thread
from time import sleep
from weakref import *
class A(object):pass
def callback(x):print'callback'
lst=[str()]
e=A()
e.c=e
wr=ref(e,callback)
del e
start_new_thread(lambda:lst.append(1),())
sleep(1)
e=wr()
del e
print('D0ne')
from weakref import *
from thread import start_new_thread
from time import sleep
class A(object):pass
def callback(x):print'Removing object'
lst=[str()]
e=A()
e.c=e
wr=ref(e,callback)
del e
start_new_thread(lambda:lst.append(1),())
sleep(1)
e=wr()
del e
print'D0ne'
from weakref import *
from thread import start_new_thread
from time import sleep
class A(object):pass
def callback(x):print'Removing object
