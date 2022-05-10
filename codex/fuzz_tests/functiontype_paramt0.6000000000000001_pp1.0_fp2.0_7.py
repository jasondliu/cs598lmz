from types import FunctionType
list(FunctionType(lambda x:x+1, globals(), 'myfunc')(1))

# FunctionType(code, globals, name, argdefs, closure)

def add(x, y):
    return x+y

print(add)
print(add.__name__)
print(add.__code__)
print(add.__code__.co_argcount)

print(add.__code__.co_code)


def add(x, y):
    return x+y

print(add.__code__.co_code)

def add(x, y):
    return x+y

print(add.__code__.co_code)

code_object = compile('[x*x for x in range(10)]', '<string>', 'eval')
eval(code_object)

code_object = compile('[x*x for x in range(10)]', '<string>', 'exec')
exec(code_object)


code_object = compile('[x*x for x in range(10)]', '<string>
