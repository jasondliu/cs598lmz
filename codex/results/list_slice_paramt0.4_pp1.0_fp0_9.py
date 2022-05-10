import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(lst[0]))
keepali0e.append(weakref.ref(callback))
del a
del lst
import gc
gc.collect()
print keepali0e[0](),keepali0e[1](),keepali0e[2](),keepali0e[3]()
</code>
The output is:
<code>&lt;__main__.A object at 0x7f1b3c1b9a50&gt; &lt;__main__.A object at 0x7f1b3c1b9a50&gt; &lt;__main__.A object at 0x7f1b3c1b9a50&gt; &lt;function callback at 0x7f1b3c1b9c80&gt;
</code>

