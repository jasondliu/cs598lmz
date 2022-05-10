import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a,A
lst.append(str())
print(lst)

#存取属性
#描述器
class RevealAccess(object):
    """A data descriptor that sets and returns values
       normally and prints a message logging their access.
    """
    def __init__(self,initval=None,name='var'):
        self.val=initval
        self.name=name
    def __get__(self,obj,objtype):
        print('Retrieving',self.name)
        return self.val
    def __set__(self,obj,val):
        print('Updating',self.name)
        self.val=val
class MyClass(object):
    x=RevealAccess(10,'var "x"')
    y=5
m=MyClass()
print(m.x)
m.x=20
print(m.x)
print(m.y)

#类的属性和实例
