from types import FunctionType
a = (x for x in [1]) # (1)
b = [x for x in [1]] 
c = [x for x in [1] if x] # (2)
a.append(2)
a._[2]

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

## как получить список методов из объекта
from types import FunctionType
a = (1 for x in [1, 2, 3])
dir(a)
b = [x for x in [1,2, 3]]
dir(b)


from types import FunctionType

def f(x):
    return x**2

def get_list_of_object_functions(object):
    func_list = [o for o in dir(object) if type(getattr(object, o))==FunctionType]
    return sorted(func_list)

get_
