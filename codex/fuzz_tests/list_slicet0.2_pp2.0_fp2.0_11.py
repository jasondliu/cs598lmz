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
print keepali0e

#结果：
#[<weakref at 0x00000000020D5C68; to 'A' at 0x00000000020D5B88>, []]
#结论：
#在循环引用中，如果一个对象的引用计数为0，那么这个对象就会被回收，即使它还有循环引用。
#在循环引用中，如果一个对象的引用计数不为0，那么这个对象就不会被回收，即使它没有循环引用。

