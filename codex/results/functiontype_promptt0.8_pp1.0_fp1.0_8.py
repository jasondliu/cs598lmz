import types
# Test types.FunctionType
def add(x,y):
    return x+y

def use_something(x, func):
    return func(x)

print(use_something(2, lambda x: x**2))
print(use_something(2, lambda x: x**4))
print(use_something(3, add))

# Multi-函数
from functools import reduce

def add(x,y):
    return x+y

def fn(x,y):
    return x*10+y

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

def mul(x,y):
    return x*y

def str2int(s):
    return reduce(fn,map(char2num,s))

print(str2int('12345'))

# Test upper
def normalize(name):
    return name.title()

L1
