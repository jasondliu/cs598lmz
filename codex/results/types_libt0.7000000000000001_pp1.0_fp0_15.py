import types
types.MethodType(f, None, Hello)

class MyMeta(type):
    def __call__(cls, *args, **kwargs):
        print("*** MyMeta.__call__")
        obj = cls.__new__(cls)
        cls.__init__(obj, *args, **kwargs)
        return obj
    
class MyClass(metaclass=MyMeta):
    def __new__(cls, *args, **kwargs):
        print("*** MyClass.__new__")
        return object.__new__(cls)
    
    def __init__(self, *args, **kwargs):
        print("*** MyClass.__init__")
        self.attr = args[0] if args else None

y = MyClass(42)
y.attr

class MyMeta(type):
    def __init__(cls, name, bases, namespace):
        print("*** MyMeta.__init__")
        super().__init__(name, bases, namespace)
        cls.attr = 42
        

