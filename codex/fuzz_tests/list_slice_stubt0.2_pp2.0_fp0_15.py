import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)
</code>
Output:
<code>['', &lt;weakref at 0x7f8c8c0d9b88; to 'A' at 0x7f8c8c0d9b48&gt;]
</code>

