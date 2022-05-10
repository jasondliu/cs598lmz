from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__()))
print(type(a.__next__().__next__))
print(type(a.__next__().__next__()))
print(type(a.__next__().__next__().__next__))
print(type(a.__next__().__next__().__next__()))

# 可以看到，generator的__next__()方法是一个generator，
# 所以，generator的__next__()方法可以被调用多次，
# 但是每次调用都会返回一个新的generator，
# 所以，generator的__next__()方法只能被调用一
