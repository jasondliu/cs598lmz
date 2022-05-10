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
#[<weakref at 0x000002A6F7E8D848; to 'A' at 0x000002A6F7E8D7F0>, []]
#结论：
#当一个对象的引用计数为0时，会调用回调函数，并且回调函数中的参数是这个对象的弱引用。
#当一个对象的引用计数为0时，会调用回调函数，并且回调函数中的参数是这个对象的弱引用。
#当一个对
