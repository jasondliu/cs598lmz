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

# 下面这个例子会报错，因为在回调函数里面，引用计数器已经为0，所以不能再访问引用计数器
# import weakref
# class A(object):pass
# def callback(x):print(x)
# keepali0e=[]
# lst=[str()]
# a=A()
# a.c=a
# keepali0e.append(weakref.ref(a,callback))
# del a
# print(lst)

# 弱引用对象的访问
import weakref
class A(object):pass
def callback(x):print(x)
keepali0e=[]
lst=[str()]
a=A
