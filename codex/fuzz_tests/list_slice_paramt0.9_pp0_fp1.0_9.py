import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
a.c=callback
del a
del callback
del keepali0e
del lst
import gc
for obj in gc.get_objects():
    ref=weakref.getweakrefs(obj)
    if ref:
        print("ref",ref)
</code>
Ouput:
<code>ref [&lt;weakref at 0x0188A758; to 'function' at 0x01C8FAF0&gt;, &lt;weakproxy at 0x01887A58 to 'function' at 0x01C8FAF0&gt;]
</code>
My question is why there is a weakproxy, who is the weakproxy user?If the  weakproxy is the memory adress but what is the 0x01C8FAF0?


A:

The <code>0x01887A58</code> is the memory address where the <code>weakproxy</code> object is stored. <code>0x01C8FAF0</code> is where the undeleted function is stored, and the <code>weakproxy</code>
