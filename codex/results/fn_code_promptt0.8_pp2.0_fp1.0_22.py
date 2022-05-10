fn = lambda: None
# Test fn.__code__ is a code object
# Code objects have a co_code attribute that is a string representing bytecode
compiled_fn.__code__.co_code
# Show the disassembly
dis.dis(compiled_fn)

# Example
def greet(name):
    return 'Hello ' + name + '!'

greet('Guido')
# fn.__code__ is a code object
greet.__code__
# fn.__code__.co_code is a string of bytecode
greet.__code__.co_code
dis.dis(greet)

# Example: dynamic dispatch
class Spam:
    def bar(self, x):
        print('Spam.bar:', x)

class Eggs:
    def bar(self, x):
        print('Eggs.bar:', x)

# Example dispatch table
def foo(obj):
    return obj.bar
def bar(x):
    print('bar:', x)

D = {'foo': foo, 'bar': bar}
D['foo'](Spam())(7)
D
