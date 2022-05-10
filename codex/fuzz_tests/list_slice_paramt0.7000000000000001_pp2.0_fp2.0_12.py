import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(weakref.ref(lst[0],callback))
del lst
print len(keepali0e)
</code>
I am using python 2.6.
I really need a weakref that keeps the object alive but does not prevent it from being garbage collected.
I tried to implement one by myself but it's not working (I don't see the callback being called, or at least, it's not doing what I need it to do).
<code>class WeakRefToKeepAlive(weakref.ref):

    def __init__(self,object,callback):
        self.keepAlive=object
        self.keepAliveRef=weakref.ref(object,callback)

    def __call__(self):
        return self.keepAliveRef()

    def __repr__(self):
        return '&lt;WeakRefToKeepAlive object at %s&gt;' % hex(id(self))

    def __eq__(self,other):
        return id(self)==id(other)

    def __ne
