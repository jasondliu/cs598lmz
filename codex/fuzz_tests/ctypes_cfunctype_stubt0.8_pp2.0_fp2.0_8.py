import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
fun()

# __annotations__
def foo(a:'str'=3,b:'int'=4):
    pass
print(foo.__annotations__)

# 元类
def say(self,what):
    print("say {}!".format(what))
Hello=type('Hello',(object,),dict(hello=say))
h=Hello()
h.hello("world")

# 元类
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
    pass
L=MyList()
L.add(1)
print(L)
l=list()
l.add(1)
print(l)

# 元类
class Say(type):
    def __new__(cls,
