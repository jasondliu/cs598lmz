import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
</code>
I want to use the code to determine if there is a cycle in my program, but when I run the code, it will run indefinitely. Why is this so?


A:

To even keep the <code>weakref.ref</code> alive, you need to keep it in the <code>keepali0e</code> list.
<code>import gc
import weakref
class A(object):pass
def callback(x):print("callback")

keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:
    # print(len(keepali0e))
    keepali0e.append(lst[:])
    gc.collect()
# print(len(keepali0e))
</code>

