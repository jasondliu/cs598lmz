from types import FunctionType
a = (x for x in [1])
type(a)

# 判断是否是可调用对象
callable(a)
callable(lambda x:x)
callable(FunctionType)

# 判断是否是生成器
import inspect
inspect.isgenerator(a)

# 判断是否是生成器函数
inspect.isgeneratorfunction(lambda x:x)

# 判断是否是模块
import sys
inspect.ismodule(sys)

# 判断是否是类
class A:
    pass
inspect.isclass(A)

# 判断是否是方法
class A:
    def a(self):
        pass
inspect.ismethod(A.a)

# 判断是否是类型
inspect.isroutine(A.a)

#
