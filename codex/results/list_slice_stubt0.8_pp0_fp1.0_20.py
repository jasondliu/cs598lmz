import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a, callback))
#print(keepali0e)
while lst:
    pass
#print(lst)
a=A()
a.x=A()
a.x.y=a
a=a.x
#print(a)
#print(a.y)
#del a

class A(object):
    def __init__(self):
        self.x=1
    def __del__(self):
        print("del")
a=A()
a.b=a
del a

#print(help(__builtins__))
#print(dir(__builtins__))
#print(type(__builtins__))

#print(__import__("os"))
#print(__import__("math"))
#print(__import__(""))
#print(__import__("sys"))
#print(__import__("os.path"))
#print(__import__("a.b.c"))
#print(__import__("time"))
#print(__import__("
