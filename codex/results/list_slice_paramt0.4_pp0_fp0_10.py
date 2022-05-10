import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst
#<ref at 0x01E9C5B0; dead>
#['\x00']

# 使用weakref.WeakKeyDictionary()来维护一个对象的弱引用
# 当对象被回收时，它在字典中的条目也会被自动删除
# 可以用这种方法来实现一个对象的弱引用
# 可以用这种方法来实现一个对象的弱引用
import weakref
class A(object):pass
a=A()
d=weakref.WeakKeyDictionary()
d['primary']=a
print d['primary']
del a
print d['primary']

