from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code objects
import dis
dis.dis(lambda x: x)

# bytecode
def greet(name):
    return 'Hello, ' + name + '!'
greet.__code__.co_code

# bytecode instructions
def greet(name):
    return 'Hello, ' + name + '!'
greet.__code__.co_code

# bytecode instructions
def greet(name):
    return 'Hello, ' + name + '!'
greet.__code__.co_code

# bytecode instructions
def greet(name):
    return 'Hello, ' + name + '!'
greet.__code__.co_code

# bytecode instructions
def greet(name):
    return 'Hello, ' + name + '!'
greet.__code__.co_code

# bytecode instructions
def greet(name):
    return 'Hello, ' + name + '!'
greet.__code__.co_code

# bytecode instructions
def greet(name):
    return '
