import types
# Test types.FunctionType as a function.
try:
    types.FunctionType(None, None, None)
except TypeError as e:
    msg = e.args[0].split(": ")[1]
    print(str(e)[:len(msg) + 3], str(e)[len(msg) + 3:])
else:
    print("This should not happen")

# Test types.FunctionType as a type.
class Foo(types.FunctionType):
    pass

class Bar:
    __metaclass__ = Foo

F = type(Bar)

print(F, F.__bases__)
print(type(Bar))
print(Bar, Bar.__mro__)
print(type(Bar()))
