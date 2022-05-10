import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=weakref.ref(a,callback)
lst.append(a)
keepali0e.append(a)
</code>
This code works fine. The problem is that I want to remove the first element <code>lst[0]</code> after the second element <code>lst[1]</code> is deallocated. The problem is that I don't want to keep a reference to the second element <code>lst[1]</code> alive. Is there a way to do that?

