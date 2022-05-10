from _struct import Struct
s = Struct.__new__(Struct)
#staticmethod
#private method
#private
#classmethod, even the __metaclass__ can't change it's implement

class A(type):
    def __new__(_cls, *args, **kw):
        print 'A __new__', _cls
        print 'args:', args
        print 'kw:', kw
        return type.__new__(_cls, *args, **kw)

    def __getitem__(self, _item):
        print self, _item
        return self

class Foo:
    __metaclass__ = A

type(Foo)
print type(A)
print type(A) == type(type)
print type(type) == type
print type(A) is type
print type is type(type)
print A is type
print type is A
a = A()
print type(a)
#class A(Foo, type):
#    pass

#a = A()
#print a
#print type(a)

class A(type):
    def __new__(_cls,
