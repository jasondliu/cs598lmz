import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
gc.collect()
print(lst)

# 弱引用
import weakref
class ExpensiveObject(object):
    def __del__(self):
        print('(Deleting %s)' % self)
def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback(', reference, ')')
obj=ExpensiveObject()
r=weakref.ref(obj,callback)
print('obj:',obj)
print('ref:',r)
print('r():',r())
print('deleting obj')
del obj
print('r():',r())
