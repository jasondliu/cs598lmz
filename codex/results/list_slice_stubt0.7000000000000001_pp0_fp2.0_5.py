import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepalive.append(lst)
del a
lst.append(callback)
weakref.ref(lst,callback)
print lst
</code>
For <code>lst.append(a)</code> I've got <code>RecursionError: maximum recursion depth exceeded</code>
But if I comment it out, I've got <code>lst</code> printed.
It seems that the <code>a.c=a</code> is not the reason.
So what's the reason?
What's the different between <code>lst.append(a)</code> and <code>lst.append(callback)</code>?


A:

If you make <code>a</code> a global, you won't get the recursion error. 
<code>class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(lst)
lst.append(a)
