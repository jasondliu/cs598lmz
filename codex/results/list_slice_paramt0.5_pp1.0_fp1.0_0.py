import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst,callback))
del a
del lst
print(keepali0e[0]())
print(keepali0e[1]())

# 第二种情况：
# 如果一个对象在析构时需要访问其他对象，那么在访问时应该使用弱引用，因为这个其他对象有可能已经被析构掉了。
# 下面的例子中，对象a在析构时需要访问对象b，但是对象b已
