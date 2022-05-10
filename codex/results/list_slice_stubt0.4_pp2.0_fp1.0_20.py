import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.callback=weakref.ref(callback,lst)
del a
del keepalive[0]
print lst

# 输出：
# []

# 分析：
# 当对象a被删除时，a.callback引用的对象执行回调函数callback，callback函数的参数x为lst，即列表lst，执行del lst[0]，删除列表lst的第一个元素，lst变为空列表，所以输出为[]。

# 练习4：
# 写一个程序，输出如下
