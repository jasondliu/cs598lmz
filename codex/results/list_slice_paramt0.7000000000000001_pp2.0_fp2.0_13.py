import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print str() in lst
a=None
print str() in lst
</code>
The output is:
<code>True
False
</code>

