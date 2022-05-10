import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
while lst:
	print(lst[0])
	keepali0e.append(weakref.ref(lst[0],callback))
	lst.append(lst[0]+lst[0])
	del lst[0]

# 这个例子有点啰嗦，但是它说明了两个问题：
# 弱引用构造函数的第二个参数是一个可选的回调函数，它会在被引用的对象被销毁前被调用。
# 当一个对象的弱引用被调用时
