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
print keepali0e

# the above code is the solution to the question, which is a little bit tricky.

# the following is the code I wrote to solve the same problem
# the problem is that when I use the del command to delete the object a,
# the reference count of a will become 0 and a will be deleted.
# but the object a.c=a will never be deleted and the reference count of a.c will become 1
# and the reference count of a.c will never become 0 and the callback function will never be called.

class A(object):pass
def callback(x):print "del a"
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print keepali0e
