from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))
print(isinstance(a, list))

# 判断一个对象是否是可调用对象
print(callable(a))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))

# 使用__slots__
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动
