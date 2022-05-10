import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
while keepali0e:pass
def keepalive(obj):
    keepali0e.append(obj)
a=weakref.ref(a,callback)
lst.append(A())
</code>
And for gc.collect(), it has only one moving operation, is that also a cycle form?
<code>import gc
l=[]
def cycle():
    l.append(l)

cycle()
gc.collect()

print len(l)
</code>

