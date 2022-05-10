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

#析构函数
class A(object):
    def __del__(self):
        print('A.__del__')
a=A()
a.c=a
del a

#弱引用
import weakref
class A(object):pass
a=A()
a.c=a
keepali0e=weakref.ref(a)
del a
print(keepali0e())

#弱引用的析构函数
import weakref
class A(object):
    def __del__(self):
        print('A.__del__')
a=A()
a.c=a
keepali0e=weakref.ref(a)
del a
print(keepali0e())

#弱引用的析构函数
import weakref
class A(object):
    def __del__(self):
        print('A.__del__')
a
