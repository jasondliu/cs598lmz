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
for i in range(10):print i

# A program to create an infinite loop
lst = [1,2,3]
for i in range(10):
    lst=[2*lst[0]]
    print i

# A program to create an infinite loop
import weakref
class A(object): pass
def callback(x):
    del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
del a
while lst: keepalive.append(lst[:])
for i in range(10):
    print i

# A program to create an infinite loop
import random
def fun(i):
    if not i: return
    fun(i-1)
    fun(i-1)
fun(5)
print "hello"

# A program to create an infinite loop
import random
def fun(i):
    if not i: return
    fun(i-1)
    fun(i-1)
