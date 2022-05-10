import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print(lst)
print(keepali0e)

# 弱引用的回调函数
# 弱引用的回调函数是在对象被垃圾回收时调用的，回调函数的参数是弱引用对象本身。
# 回调函数的返回值被忽略。
# 回调函数不能引用被回收对象，否则会引发异常。
# 回调函数不能保证被调用，因为垃圾回收
