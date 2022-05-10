import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
wr=weakref.ref(a,callback)
del a
keepali0e.append(lst)
del keepali0e
import gc
gc.collect()
del gc
for x in lst:
    print x
</code>
I need the result of this program is "str" after the collect
but the real result is:
<code>Exception AttributeError: "'NoneType' object has no attribute 'c'" in &lt;bound method A.__del__ of &lt;__main__.A object at 0x00000000032D9390&gt;&gt; ignored
</code>
I know that the callback has not been invoke.
I am wondering why it is the case?I want to know the reason.


A:

The issue is that you have a cycle. Your A instance is still referenced. I don't see how your program is going to produce the output you expect. Try running your example with a debug command:
<code> python -m pdb -c continue yourprogram.py 
</code>
Then type at the debugger
