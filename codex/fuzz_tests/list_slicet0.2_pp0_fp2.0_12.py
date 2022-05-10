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

#输出：
#[<weakref at 0x0000023C9B0C6F08; to 'A' at 0x0000023C9B0C6E48>, []]

#结论：
#当一个对象的引用计数为0时，它会被垃圾回收器回收，但是，如果它还存在循环引用，那么它就不会被回收。
#弱引用可以解决循环引用的问题，当一个对象只被弱引用引用时，它就会被
