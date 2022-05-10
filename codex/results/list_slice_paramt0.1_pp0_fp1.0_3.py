import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果：
#['<__main__.A object at 0x7f8f9a9b8d50>']

#这个例子中，a对象的弱引用被放在了keepalive列表中，
# 因此a对象不会被回收，而a对象的c属性指向了a对象本身，
# 因此a对象也不会被回收。
# 当a对象被回收时，回调函数callback会被调用，
# 回调函数callback会删除
