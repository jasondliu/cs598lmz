import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
del a
print(lst)

# 弱引用的一个重要特性是它们不会阻止其引用的对象被垃圾回收。

# 弱引用是使用 weakref 模块中的弱引用类创建的。
# 弱引用类接受一个可选的回调函数，它会在引用的对象被垃圾回收时被调用。
# 弱引用对象的值可以使用其 weakref 属性访问。
# 弱引用的一个重要特性是它
