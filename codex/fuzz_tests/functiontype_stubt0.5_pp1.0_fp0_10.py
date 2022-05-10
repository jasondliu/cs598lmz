from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])

def print_next(it):
    print(next(it))

print_next(a)
print_next(b)
print_next(c)

print(isinstance(print_next, FunctionType))

print_next.__code__.co_varnames

print_next.__code__.co_argcount

print_next.__code__.co_argcount

print_next.__code__.co_argcount

print_next.__code__.co_argcount

print_next.__code__.co_argcount

print_next.__code__.co_argcount

print_next.__code__.co_argcount

print_next.__code__.co_argcount

print_next.__code__.co_argcount

print_next.__code__.co_argcount

print_next.__code__.co_argcount

print_next.__code__.co
