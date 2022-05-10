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

# 弱引用
# 弱引用不会增加对象的引用计数，因此不会阻止对象被垃圾回收。
# 弱引用的一个主要用途是在数据结构中，如字典或者集合中，以防止循环引用。
# 弱引用只能引用对象，不能引用函数或者类。
# 弱引用不能用于判断对象是否存在，因为它可能会在
