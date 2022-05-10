from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

def f():
    yield 1
    yield 2
    yield 3

print(type(f()))
print(type(f().__next__))
print(type(f().__next__) == FunctionType)

print(type(f))
print(type(f) == FunctionType)

print(type(f) == type(f()))
print(type(f) == type(f().__next__))
print(type(f) == type(f().__next__) == FunctionType)

print(type(f) == type(f().__next__) == type(f().__next__) == FunctionType)

# print(type(f) == type(f().__next__) == type(f().__next__) == type(f().__next__) == FunctionType)

print(type(f) == type(f().__next__) == type(f().__next__) == type(f().
