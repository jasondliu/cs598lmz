from types import FunctionType
list(FunctionType(lambda x:x**2,globals(),'func') for x in range(3))

# 代码在Python2.6.5中运行正常

# 总结：
# lambda 只是一个表达式，不是语句；lambda的主体是一个表达式，而不是代码块，仅仅能在lambda表达式中封装有限的逻辑进去
# lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来
