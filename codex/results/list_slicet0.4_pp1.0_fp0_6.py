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
print(keepali0e)
</code>
I got this error:
<code>Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\test.py", line 13, in &lt;module&gt;
    while lst:keepali0e.append(lst[:])
MemoryError
</code>
I don't know why.


A:

The problem is that you're creating an infinite loop here:
<code>while lst:keepali0e.append(lst[:])
</code>
The <code>callback</code> function is being called, but the <code>while</code> loop continues to loop until it runs out of memory.

