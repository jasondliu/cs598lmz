from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 生成器函数
def gen():
    i = 0
    while True:
        i += 1
        yield i

# 生成器函数
def gen2():
    i = 0
    while True:
        i += 1
        return i

# 生成器函数
def gen3():
    i = 0
    while True:
        i += 1
        return i

def gen4():
    i = 0
    while True:
        i += 1
        return i

def gen5():
    i = 0
    while True:
        i += 1
        return i

def gen6():
    i = 0
    while True:
        i += 1
        return i

def gen7():
    i = 0
    while True:
        i += 1
        return i

def gen8():
    i = 0
    while True:

