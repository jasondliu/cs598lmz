import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print lst
print keepalive

#[str(), <weakref at 0x7f8a6a8b6f28; to 'A' at 0x7f8a6a8b6d68>]
#[<__main__.A object at 0x7f8a6a8b6d68>]

#第一个元素是字符串，第二个元素是弱引用对象，弱引用对象的回调函数是callback，
# 回调函数的参数是弱引用对象，回调函数的功能是删除lst列表的第一个元素，
