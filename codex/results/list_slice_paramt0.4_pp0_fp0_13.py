import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

# 析构函数
class A(object):
    def __del__(self):
        print("I'm dying")
a=A()
del a

# 析构函数是否被调用
class A(object):
    def __del__(self):
        print("I'm dying")
a=A()
a.b=a
del a

# 析构函数是否被调用
class A(object):
    def __del__(self):
        print("I'm dying")
a=A()
a.b=a
del a.b

# 析构函数是否被调用
class A(object):
    def __del__(self):
        print("I'm dying")
a=A()
a.
