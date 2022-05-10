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

#类的属性
class A(object):
    def __init__(self):
        self.name='python'
    def getName(self):
        return self.name
a=A()
print(a.name)
print(a.getName())

#类的方法
class A(object):
    def __init__(self):
        self.name='python'
    def getName(self):
        return self.name
a=A()
print(a.name)
print(a.getName())

#类的方法
class A(object):
    def __init__(self):
        self.name='python'
    def getName(self):
        return self.name
a=A()
print(a.name)
print(a.getName())

#类的方法
class A(object):
    def __init__(self):
        self.name='python'
    def getName(
