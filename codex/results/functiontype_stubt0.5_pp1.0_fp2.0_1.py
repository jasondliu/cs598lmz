from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda x: x))
print(type(FunctionType))
print(type(FunctionType(lambda x: x, {})))

# 2. 内建函数
print(type(abs))  # <class 'builtin_function_or_method'>
print(type(open))  # <class 'builtin_function_or_method'>
print(type(int))  # <class 'type'>
print(type(str))  # <class 'type'>
print(type(dict))  # <class 'type'>
print(type(list))  # <class 'type'>
print(type(tuple))  # <class 'type'>
print(type(set))  # <class 'type'>
print(type(object))  # <class 'type'>

# 3. 模块
import sys
print(type(sys))  # <class 'module'>

# 4. 类
class MyClass:
    pass

print(type(MyClass))  # <class 'type
