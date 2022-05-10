import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
keepali0e.append(lst)
trash=[]
for i in xrange(100):trash.append(str())
del trash
print len(lst)
del keepali0e
print len(lst)
</code>
What happens is that the callback is not called and <code>lst</code> is not deleted.
Can someone explain what is happening?


A:

The problem with your example is that you're creating a circular reference. The <code>a</code> object has a reference to itself, so it's not going to be garbage collected at all.
This, on the other hand, works just fine:
<code>import weakref
class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
keepalive.append(weakref.ref(a,callback))
del a
keepalive.append(lst)
trash=[]
for i in xrange(100):trash.append(str())
del trash
print
