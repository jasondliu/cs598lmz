import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
print(lst)
del a
print(lst)

#类的描述符
class Descriptor(object):
    def __init__(self,name=None,**opts):
        self.name=name
        for key,value in opts.items():
            setattr(self,key,value)
    def __set__(self,instance,value):
        instance.__dict__[self.name]=value
class Typed(Descriptor):
    expected_type=type(None)
    def __set__(self,instance,value):
        if not isinstance(value,self.expected_type):
            raise TypeError('expected '+str(self.expected_type))
        super(Typed,self).__set__(instance,value)
class Unsigned(Descriptor):
    def __set__(self,instance,value):
        if value<0:
            raise ValueError('Expected >=0')
