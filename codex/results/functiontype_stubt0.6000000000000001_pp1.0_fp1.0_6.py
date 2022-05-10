from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# isinstance 与type的区别在于：type只能判断一层，而isinstance可以判断多层
# 当我们用isinstance()判断一个对象是否是函数时，实际上，在判断过程中，
# 它检查了对象的__class__属性，如果该属性是某个类型，则返回True；
# 如果该属性是另一个类型，但该类型是前一个类
