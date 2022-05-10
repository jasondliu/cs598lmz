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
To make a long story short, the action of adding <code>keepali0e.append(lst[:])</code> to the end of the code made it run forever. When I removed it (commented it out), the code ran just fine, but then I found that <code>lst</code> was empty.
So, my question is, was <code>lst</code> empty, or was there a string in <code>lst</code> that just happened to be printed out?
EDIT: The above code is from this question, not my answer, in case you're wondering.

