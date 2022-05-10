import types
types.FunctionType

# also useful
types.ModuleType
types.MethodType
types.BuiltinFunctionType
types.BuiltinMethodType
types.ClassType
types.InstanceType
types.TypeType

# -->
# check different types
isinstance(1, int)
isinstance([], list)
isinstance(lambda x: x, types.FunctionType)
isinstance('s', str)

# type error
1 + 's'


# custom types
class Foo(object):
    bar = True

f = Foo()

print(f)
print(f.bar)
print(f.__class__)
print(Foo.bar)

type(f)
type(Foo)


# custom types
class Foo(object):
    def __init__(self, val):
        self.val = val

f = Foo(3)
f.val

f.__dict__

# slots!
class Foo(object):
    __slots__ = ['val']

    def __init__(self, val):
        self.val = val

