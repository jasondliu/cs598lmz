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
</code>
This code runs great in Python 2.7. However, it seems that the callback function will not be called in Python 3.x. I would like to know whether this is a bug in Python or a feature that I don't understand.
Update:
the problem only appear in Python 3.4. In Python 3.2 and 3.3, the program will not be blocked.

