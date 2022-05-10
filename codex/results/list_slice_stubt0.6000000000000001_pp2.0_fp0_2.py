import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
for i in range(100):
    lst[0]=(i,callback,weakref.ref(lst))
    callback(lst)
print lst
</code>
Output:
<code>$ python test.py
[(99, &lt;function callback at 0x7f87aad2f8c0&gt;, &lt;weakref at 0x7f87aad2f7c0; dead&gt;)]
</code>

