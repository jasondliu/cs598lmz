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
del a
lst[0]

#测试一个类的实例是否可以作为一个字典的key
class A(object):
    def __init__(self,name):
        self.name=name
    def __hash__(self):
        return hash(self.name)
    def __eq__(self,other):
        return self.name==other.name
a=A('a')
b=A('b')
d={a:1,b:2}
print(d[a])
print(d[b])

#测试一个类的实例是否可以作为一个字典的key
class A(object):
    def __init__(self,name):
        self.name=name
    def __hash__(self):
        return hash(self
