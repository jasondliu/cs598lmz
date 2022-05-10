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

#最后一个输出的是列表的内存地址，而不是列表的内容，因为列表的内容已经被删除了，所以只能打印列表的内存地址
#这个例子说明了，弱引用对象被删除时，会调用回调函数，这个回调函数可以是任意的函数，函数的参数是引用对象本身

#也可以用弱引用来实现
