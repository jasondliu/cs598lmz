import types
# Test types.FunctionType
message = "Hello!"
def say_hello():
    print(message)

def change_message(new_message):
    global message
    message = new_message
    print(message)

print(type(say_hello) == types.FunctionType)
print(type(change_message) == types.FunctionType)

# Test types.LambdaType
double = lambda x: x * 2
print(type(double) == types.LambdaType)

# Test types.GeneratorType
def even_integers_generator(n):
    i = 0
    while i < n:
        yield i * 2
        i += 1

print(type(even_integers_generator(10)) == types.GeneratorType)

# Test types.MethodType
class Foo(object):
    def foo(self):
        return self

foo_instance = Foo()
print(type(foo_instance.foo) == types.MethodType)
print(type(Foo.foo) == types.MethodType)

# Test types.BuiltinFunctionType

