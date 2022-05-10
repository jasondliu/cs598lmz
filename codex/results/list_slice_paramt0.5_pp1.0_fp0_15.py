import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print lst
lst=['a']
gc.collect()
print lst

#weakref.ref(obj[,callback])
#返回一个弱引用对象，它引用对象obj。当obj被删除时，弱引用对象将被删除。
#当obj被删除时，如果callback参数被指定，它将被调用。

#weakref.WeakKeyDictionary([dict])
#返回一个新的弱引用字典。字典的键是弱引用的，并且仅仅当它们的目标对象被删
