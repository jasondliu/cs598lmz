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

# 弱引用的回调函数可以在对象被垃圾回收时被调用。
# 回调函数的参数是弱引用对象本身。
# 回调函数的返回值被忽略。
# 回调函数不能引发异常。
# 回调函数可以是None。
# 回调函数不能是一个循环引用。
# 回调函数不能引用回调参数。
# 回调函数不能引用回调参数
