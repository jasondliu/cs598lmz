import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a,callback,keepali0e,sys.modules["__main__"]
gc.collect()
print len(lst)
</code>
output: 1
Note:
I'm using Python 2.7.1, and I raise this bug on python issues list: http://bugs.python.org/issue14589

