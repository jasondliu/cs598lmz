from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def gen():
    yield 1

print(isinstance(gen(), GeneratorType))
print(isinstance(gen(), FunctionType))

def gen2():
    return 1

print(isinstance(gen2(), GeneratorType))
print(isinstance(gen2(), FunctionType))

'''
True
False
True
True
False
False
'''

def gen3():
    yield 1
    yield 2
    yield 3

for i in gen3():
    print(i)

'''
1
2
3
'''

def gen4():
    yield 1
    yield 2
    yield 3
    return

for i in gen4():
    print(i)

'''
1
2
3
'''

def gen5():
    yield 1
    yield 2
    yield 3
    return 'done'

for i in gen5():
    print(i)

'''
1
2
3
'''

def
