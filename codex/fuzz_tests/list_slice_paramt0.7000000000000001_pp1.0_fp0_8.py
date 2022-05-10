import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
keepali0e.clear()
print(lst)

#9.2.2 弱引用的使用场景
import weakref
import gc
class ExpensiveObject(object):
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print('(Deleting %s)'%self)
def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback({!r})'.format(reference))
obj=ExpensiveObject('My Object')
obj_id=id(obj)
print(obj_id)
r=weakref.ref(obj,callback)
print(r)
print('obj:',obj)
print('ref:',r)
print('r():',r())
print('deleting obj')
del obj
print('r():',r())
#回收内存
gc.collect()
print('r():',r())
print(r==None)
print
