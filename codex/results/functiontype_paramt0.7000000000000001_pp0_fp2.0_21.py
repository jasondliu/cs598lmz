from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_code)[0]
#'\x64'
isinstance(lambda: None, FunctionType)
#True

#isinstance(object, class-or-type-or-tuple)
#object is an instance of classinfo
#classinfo: class object, or a tuple of class objects
#returns True if object is an instance of classinfo
#if object is not an object of the given type, the function always returns False
#if classinfo is a tuple of types, isinstance() will return True if object is an instance of any of the types in class
#if classinfo is not a class, type, or tuple of classes, types, and such tuples, a TypeError exception is raised
#the following is from the Python tutorial
class Foo(object):
    pass
foo = Foo()
isinstance(foo, Foo)
#True
isinstance(Foo, type)
#True
isinstance(foo, object)
#True

#issubclass(class, classinfo)
#class is a subclass (direct, indirect, or virtual) of classinfo
