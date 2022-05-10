import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a;
keepalive.append(a)
lst[0]='\x05\x00\x00\x00\x00\x00\x00\x00\x03\x00'
tb = weakref.finalize(a,callback,lst,weakref.REF(lst),globals())
tb.atexit()
del a
while len(lst):print(lst)
</code>
The <code>lst</code> string is a bytes object which is the representation of an integer in python2. The code works perfectly on 32-bit python2 and python3, while it seems that the callback is called in the 64-bit version of python.
The bug can be also reproduced in <code>ipython-5.5.0</code> by running the following commands:
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a;
keepalive.append(a)
lst[0]
