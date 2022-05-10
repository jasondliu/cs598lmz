import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(A, callback))
del a
del A
lst=[]
keepalive0.append(a)
del keepalive0
print("Finish delete")
</code>
When I run this code, there is not printed "Finish delete". I want to make python garbage collection working but I don't know how to do it. I tried gc.collect() but it didn't work.


A:

There are two issues with your code:

Your code is leaking <code>a</code>s namespace, which is holding a reference to <code>a</code>s <code>__dict__</code>, which keeps a reference to <code>a.c</code>. Change <code>keepalive0.append(a)</code> to <code>keepalive0.append(a.__dict__)</code>.
Your <code>callback</code> is deleting <code>lst[0]</code> only for the first time <code>a</code> dies. Either change <code>del lst[0]</code> to <code>if '
