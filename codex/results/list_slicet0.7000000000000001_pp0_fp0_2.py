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
print 'lst:',lst
print 'keepali0e:',keepali0e
</code>
and the output is:
<code>lst: []
keepali0e: []
</code>
So the callback function is not called. I know that I can use <code>weakref.finalize</code> to call the callback function. But I just want to know what's wrong with my code.

