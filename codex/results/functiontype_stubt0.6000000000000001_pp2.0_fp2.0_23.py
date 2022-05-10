from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

def hi(name):
    return 'Hi, ' + name + '!'
print(hi('Michael'))

f = hi
print(f('Michael'))
print(f)
print(type(f))

def hi(name):
    print('Hi, ' + name + '!')

hi('Michael')
hi('Sarah')

def hi(name):
    def greet():
        return 'Hello, ' + name + '!'
    return greet

hi('Michael')
print(hi('Michael'))
f = hi('Michael')
print(f)
print(f())

def hi(name):
    def greet():
        return 'Hello, ' + name + '!'
    return greet()

print(hi('Michael'))

def hi(name):
    def greet():
        return 'Hello, ' + name + '!'
    return greet

print(hi('Michael'))
print(isinstance(hi('Michael'), FunctionType))
print(hi('Michael')())

def hi():
