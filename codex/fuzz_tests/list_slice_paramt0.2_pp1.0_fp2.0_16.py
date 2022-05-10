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
print lst

#结果：
#['\x00']

#结论：
#当一个对象的弱引用被删除时，它的回调函数会被调用。
#回调函数可以访问弱引用的弱引用对象，但是不能访问弱引用对象本身。
#回调函数可以访问弱引用对象的属性。
#回调函数可以访问弱引用对象的
