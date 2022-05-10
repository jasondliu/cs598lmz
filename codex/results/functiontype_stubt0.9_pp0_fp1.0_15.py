from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

b = [1, 2, 3]
print(type(b))
print(isinstance(b, ListType))

print(isinstance(1,int))
print(isinstance(1,StringType))
print(isinstance(1,ClassType))
print(isinstance(1,TupleType))

'''
 函数名的实质性
 对于任一对象 x ，都可以通过 type(x) 来获取 x 的类型。根据类型来决定如何做下一步
'''
def fn():
    pass
