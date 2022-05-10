import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)

del a
while lst:
    try:
        callback(lst[0])
    except TypeError:
        pass
</code>
You can take some inspiration from the <code>__del__</code> method of a subclass of <code>list</code> in that code and reuse it.

