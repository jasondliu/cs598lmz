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
        print(keepali0e[-1])
        break
</code>
I have this code,I want to know the list keepali0e[0] and keepali0e[1] refer to which object.And I want to know how long it took to add keepali0e1.


A:

I am assuming that you are trying to run a reference cycle. If that is true, I believe this is what you are asking for.
<code>import weakref
import time

class A(object):pass
def callback(x):del lst[0]
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
a=None

start=time.time()
while lst:keepalive.append(lst[:])
end=time.time()
print(keepalive[-1])
print("It took: %.10f seconds"%(end-start))
</code>
The output was:
<code>[]
It took: 0.
