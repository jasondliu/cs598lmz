import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
gc.collect()
print lst

#编写一个类，它有一个属性，可以通过实例和类访问，并且可以通过实例和类修改该属性的值
class A(object):
    _a=1
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self,value):
        self._a=value
    @a.deleter
    def a(self):
        del self._a
    @classmethod
    def get_a(cls):
        return cls._a
    @classmethod
    def set_a(cls,value):
        cls._a=value
    @classmethod
    def del_a(cl
