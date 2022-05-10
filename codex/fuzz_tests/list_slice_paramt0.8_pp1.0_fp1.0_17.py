import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
b=a
del keepali0e[:]
lst[0] = 'abc'
</code>
It seems that reference cycle keeps str object alive. Is it correct?

