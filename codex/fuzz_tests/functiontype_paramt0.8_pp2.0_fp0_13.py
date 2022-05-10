from types import FunctionType
list(FunctionType(map))

def list(fn, iterable):
    res = []
    for item in iterable:
        res.append(fn(item))
    return res

li = [1, 2, 3, 4, 5 ,6 ,7]
list( lambda x: x ** 2, li)
"""
"""
def list(fn, iterable):
    res = []
    for item in iterable:
        res.append(fn(item))
    return res

li = [1, 2, 3, 4, 5 ,6 ,7]
list( lambda x: x ** 2, li)
"""
"""
def list(fn, iterable):
    res = []
    for item in iterable:
        res.append(fn(item))
    return res

def filter(predicate, iterable):
    res = []
    for item in iterable:
        if predicate(item):
            res.append(item)
    return res

def map(fn, iterable):
    filtered = filter(lambda x: x is not None, iterable)
    return list
