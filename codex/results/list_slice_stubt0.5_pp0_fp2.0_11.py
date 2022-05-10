import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
a.b=weakref.WeakKeyDictionary(a,callback)
del a
#del lst[0]
#print(lst)
print(keepali0e)
</code>

