import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
del a
del keepalive
del lst
gc.collect()
</code>
Result:

Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import gc
>>> import weakref
>>> class A(object):pass
...
>>> def callback(x):del lst[0]
...
>>> keepali0e=[]
>>> lst=[str()]
>>> a=A()
>>> a.c=a
>>> keepalive.append(a)
>>> lst.append(a)
>>> lst.append(weakref.ref(a,callback))
>>> del a
>>> del keepalive
>>> del lst
>>> gc.collect()
1
>>>

Python 2.6.2 (r262:71600
