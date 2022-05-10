import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
print lst

#结果：
#['\x00']
#结论：
#当一个对象的弱引用被删除时，它的回调函数会被调用，但是当一个对象的强引用被删除时，它的回调函数不会被调用。
#当一个对象的弱引用被删除时，它的回调函数会被调用，但是当一个对象的强引
