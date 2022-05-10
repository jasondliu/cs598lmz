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
print('1=====',lst)
class B(object): pass
def callback(x): del lst[0]
keepalive = []
lst = [str()]
b = B()
b.c = b
keepalive.append(weakref.ref(b, callback))
keepalive.append(weakref.ref(b.c, callback))
del b
print('2======', lst)
# print(lst.__len__())

# 弱引用也可以指定回调函数，在指向的对象被销毁时调用，例如：
# class Foo(object):
#     def __init__(self, name):
#         self.name = name
#     def __del__(self):
#         print('Dead', self
