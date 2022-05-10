from types import FunctionType
a = (x for x in [1])
print(type(a))

print(type(dict))
print(type(dict()))
print(type(FunctionType))
print(type(FunctionType()))

# 只有在使用函数的时候，才会有 type(函数名) = FunctionType
# 只有在通过构造器创建对象的时候，才会 type(对象名) = 对象类型

# 6.内建函数
# 可以用dir查看
dir(__builtins__)


# 下划线的使用
# 1.解释器会把没有被当做变量名使用的下划线替
