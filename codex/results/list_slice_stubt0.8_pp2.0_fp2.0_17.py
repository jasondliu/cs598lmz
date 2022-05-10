import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append((weakref.ref(a,callback),lst))
del a
for i in range(100):
    try:del lst[0]
    except:pass
</code>
It is actually even worse in Python 2.5.
I would like to know what is the best way to crash the Python Interpreter (2.4 and 2.5) for testing a debugger.

