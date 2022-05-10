from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(FunctionType))

# 判断一个对象是否是函数
def fn():
    pass

print(callable(fn))
print(callable(lambda x: x))
print(callable(abs))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))

# 使用__slots__
# 在Python中，每个类都有一个__dict__属性，用来存储实例的属性。如果不使用__slots__，那么在创建实例的时候，每个实例都会创建一个__dict__属性，用来存储
