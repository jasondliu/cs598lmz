import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
lst.append(weakref.ref(lst[0],callback))
del lst
print('ok')

# 这个例子中，lst[0]是一个空字符串，lst[1]是一个A实例，lst[2]是对lst[0]的弱引用。
# 当lst被删除时，lst[0]被回收，然后lst[2]的回调被调用，从lst中删除lst[1]。
# 如果lst[1]中的循环引用被清理，那么lst[1]也会被
