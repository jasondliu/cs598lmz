import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)

#结果：
#[<weakref at 0x0000020A8B8B9F88; to 'A' at 0x0000020A8B8B9F48>, ['']]

#结论：
#当一个对象的引用计数为0时，会调用__del__方法，但是如果对象的__del__方法中又引用了自己，那么这个对象的引用计数就不会为0，
#也就不会调用__del__方法，这样就会导致内存泄漏。
#当一个对象的引用
