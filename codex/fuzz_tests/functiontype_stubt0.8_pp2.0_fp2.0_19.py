from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(print))
print(isinstance(print, FunctionType))

# 实例属性和类属性
# 类属性归类所有，与实例无关。实例属性是不能直接访问的，要通过实例变量访问
# 通过实例变量访问实例属性时，如果实例属性不存在，就会查找类属性，如果类属性也不存在，就报错
# 通过实例
