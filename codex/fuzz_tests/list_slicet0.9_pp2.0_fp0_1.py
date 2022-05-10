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
end=time.clock()
print end-start
</code>


A:

There is a pretty large difference.  For starters, the <code>str()</code> inside <code>[]</code> is different from the expression <code>str()</code> alone -- the former constructs a list containing one element, the latter constructs an empty string (an instance of <code>str</code>), which is then discarded.  Using the latter, <code>del lst[0]</code> is a no-op, as is using <code>lst[:]</code>, which returns a shallow copy but modifies nothing.
That last one is also creating a <code>list</code> each time through the loop -- that alone might make the entire script around 100 times slower.  Using the alternative <code>if lst</code> may be faster, depending on how Python optimizes it.
Perhaps this would be a bit closer:
<code>import time
start=time.clock()
def recur(i):
    if i==0:
        return None
    else:
        return recur(i-1)
