from types import FunctionType
list(FunctionType(FunctionType.__code__, globals(), 'my_func')())

# 你想获取一个函数的源代码字符串
# 函数本身没有源代码字符串属性，但是其代码对象有：
import inspect
import example
print(inspect.getsource(example.a))
print(inspect.getsource(example.c))
print(inspect.getsource(example.f))

# 你想获取一个函数的注解（annotation）
# 注解是函数的属性，可以在函数定义的时候指定：
def add(x:int, y:int) -> int:
   
