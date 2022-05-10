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

# 按照预期，每次循环都会删除列表中的一个元素，知道列表为空，回调函数被调用，删除弱引用，然后程序结束
# 实际上，程序一直在循环，因为弱引用不会被删除，因为它引用的对象有一个循环引用
# 实际上，弱引用指向的对象也没有被删除
