from types import FunctionType
list(FunctionType(lambda x:x, {}, 'lambda_name', (1,2), None).__closure__)[0].cell_contents(4)

print()
print('------------- 8')
print()

print(__import__('sys').getrecursionlimit())

print()
print('------------- 9')
print()

import builtins
print(dir(builtins))

print()
print('------------- 10')
print()

def a():
    print('a()')

def b():
    print('b()')
    a()

def c():
    print('c()')
    b()

c()

print()
print('------------- 11')
print()

def c():
    print('c()')
    b()

def b():
    print('b()')
    a()

def a():
    print('a()')

c()

print()
print('------------- 12')
print()

def a():
    print('a()')
    b()
    c()

def b():
    print('b()')


