import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
#print(keepali0e)

#5.5 替换内部变量
class C(object):pass
a=C()
a.x=1
a.y=1
b=C()
b.x=2
b.y=2
#print(a.__dict__)
#print(b.__dict__)
a.__dict__,b.__dict__=b.__dict__,a.__dict__
#print(a.__dict__)
#print(b.__dict__)

#5.6 访问对象的私有属性
class MyClass(object):
    def __init__(self):
        self.__superprivate='Hello'
        self._semiprivate='World'
mc=MyClass()
#print(mc._MyClass__superprivate)
#print(mc._semiprivate)
#print(dir(mc))
#print(mc.__dict__)

#5.7 创
