import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
len(lst)

#Output: 1

def callback(x):x.append(1)
l=[]
keepali0e=[l]
callback(l)
len(l)

#Output: 1
#Seems to get around the 'callback doesn't work' problem.

class A(object):pass
lst=[]
lst.append(A())
lst.append(lst[0])
lst[0].c=lst[1]
len(lst)

#Output: 2

class A(object):pass
def callback(x):x.append(1)
l=[]
keepali0e=[l]
l.append(A())
l[0].c=l[0]
keepali0e.append(weakref.ref(l[0],callback))
len(l)

#Output: 1
#Doesn't fall into the 'callback doesn't work' trap.
</code>


A:

<code>weakref.ref(x, callback)</code> creates a weak reference to
