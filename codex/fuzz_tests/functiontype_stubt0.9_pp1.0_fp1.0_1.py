from types import FunctionType
a = (x for x in [1])
print(type(a))

def fun():
    yield 1
    yield 2

print(type(fun))
print(type(fun()))
print(type(fun().__next__))

print(eq(list,list))
print(eq([],[],2))
print(eq(eq,[1],[2],3))
