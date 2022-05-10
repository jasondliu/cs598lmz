import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

# 创建一个弱引用，并将其传递给回调函数。
# 回调函数将删除列表中的第一个元素。
# 创建一个类的实例，并将其赋值给一个属性。
# 将实例添加到列表中。
# 删除实例。
# 打印列表。
# 运行结果：
# ['a']
# 创建一个类的实例，并将其赋值给一个属性。

