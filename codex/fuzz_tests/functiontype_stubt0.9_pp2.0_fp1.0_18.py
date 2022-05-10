from types import FunctionType
a = (x for x in [1])

print(type(a))
print(isinstance(a, Iterator))
print(type(lambda x: x))


# In [5]:

def has_Yield(func):
    if isinstance(func, FunctionType):
        return 'yield' in func.__code__.co_names
    else:
        return False

def my_generator(n):
    for i in range(n):
        yield i

def my_function(n):
    yield 1234
    return

print(has_Yield(my_generator))
print(has_Yield(my_function))


# In [6]:

f = (x for x in [1])
print(isinstance(f, Iterator))
print(has_Yield(f))

f = my_generator(3)
print(isinstance(f, Iterator))
print(has_Yield(f))


# In [7]:

foo = (x for x in [1, 2, 3])
bar = my_generator(5)


