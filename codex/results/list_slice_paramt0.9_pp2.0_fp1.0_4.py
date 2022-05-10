import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
print"count:%d"%sys.getrefcount(a)
ref=weakref.ref(a)
</code>
why the result of function sys.getrefcount is printed out three?
Isn't the 'a' referenced by itself twice and referenced by a weak reference once?

