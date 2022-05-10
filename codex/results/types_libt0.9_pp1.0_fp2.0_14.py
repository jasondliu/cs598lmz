import types
types.MethodType(myFn, 'str')  # TypeError
</code>
Alternatively, you could use a metaclass:
<code>class MyType(type):
    def __prepare__(mcs, name, bases):
        return {}  # to avoid a MappingProxy

    def __new__(mcs, name, bases, namespace):
        namespace['myFn'] = lambda: None
        cls = super().__new__(mcs, name, bases, namespace)
        return cls

class MyClass(metaclass=MyType):
    pass

MyClass.myFn()  # None
</code>

