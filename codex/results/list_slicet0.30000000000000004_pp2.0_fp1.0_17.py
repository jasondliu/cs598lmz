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
#[<weakref at 0x7f6e0c2d8e18; to 'str' at 0x7f6e0c2d8e18>, []]

#结论：
#当对象a被删除时，它的弱引用对象被回调函数删除，但是a.c指向a，所以a还存在，因此a的弱引用对象不会被删除。
#由于a的弱引用对象不会被删除，所以lst不会被删除，因此while循环不会
