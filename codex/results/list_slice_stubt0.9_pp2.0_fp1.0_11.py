import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.d=a.e=a.f=a.g=&lt;function callback at 0x03D1C8B0&gt;
lst[0]=weakref.ref(a,a.c)
lst[0]=weakref.ref(a,a.d)
lst[0]=weakref.ref(a,a.e)
lst[0]=weakref.ref(a,a.f)
lst[0]=weakref.ref(a,a.g)
del a
</code>
In my mind, <code>a</code> should be destroyed after the 6th step. But it showed the object remained. It is also odd that if I assign a new value to the weakref, the object will be destroyed. This makes me so confused. 
In order to be more specific, I hoped to know what happens if I write code in this way
<code>&lt;code&gt;
lst[0]=weakref.ref(a,a.c)
del lst[0]
&lt;/code&gt;
</code>
Should the object
