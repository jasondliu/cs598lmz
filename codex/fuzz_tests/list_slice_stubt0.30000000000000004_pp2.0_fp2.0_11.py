import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
weakref.ref(lst[0],callback)
print(lst)
del a
print(lst)
del lst
print(keepalive)
del keepalive

#weakref.ref(object,callback=None)
#创建一个弱引用，当对象被回收时，调用callback函数
#callback函数接收一个弱引用对象作为参数
#弱引用对象的callable属性返回True，如果对象还存在，否则返回False
#弱引用对象的proxy属性返回被引用的对象，
