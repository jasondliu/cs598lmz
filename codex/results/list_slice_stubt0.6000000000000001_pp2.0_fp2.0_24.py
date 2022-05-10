import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
weakref.ref(a,callback)
del a
gc.collect()
del keepalive[0]
print(lst)
</code>
output:
<code>['&lt;__main__.A object at 0x00000000026D42E8&gt;']
</code>

