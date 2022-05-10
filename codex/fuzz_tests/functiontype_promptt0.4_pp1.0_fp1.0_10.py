import types
# Test types.FunctionType
def func():
    pass

print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.MethodType
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_score(self):
        return self.score

p = Person('Bob', 90)
print(type(p.get_score) == types.MethodType)

# Test types.UnboundMethodType
print(type(Person.get_score) == types.UnboundMethodType)

# Test types.BuiltinMethodType
print(type(str.lower) == types.BuiltinMethodType)

# Test types.ModuleType
import sys
print(type(sys) == types.ModuleType)

# Test types.TracebackType
try:
    raise Exception('
