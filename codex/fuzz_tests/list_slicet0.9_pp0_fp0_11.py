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
finally:
    for y in keepali0e:del y
</code>


A:

Code does not execute
The C level call <code>import_copy_reg()</code> is only reachable on python2 (not 3).  The original code might work on pypy though (untested).
Referencing the object
The "undescriptive object" object that is referenced in the <code>__reduce__</code> method is never actually referenced, <code>__getattribute__</code> is not called.
The callback is only called when there are no more references to the object and more specifically, when the garbage collector decides to garbage collect the object.  This seems to be the problem, at least one live reference must remain.
The <code>keepalive</code> object
<code>keepalive</code> is not necessary.  You do not run into problems with the garbage collector on the <code>lst</code> object, it is referenced through the closure and the <code>callback</code> function.
<code>lst</code> must have a <code>str</code>
