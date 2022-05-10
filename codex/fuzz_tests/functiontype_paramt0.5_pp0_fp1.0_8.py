from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# 从模块导入函数
# 把函数作为对象传递给其他函数
# 把函数作为返回值
# 使用闭包

# 可调用对象
# 对象调用运算符()，如果对象具有__call__方法，则调用__call__
# 函数是可调用的
# 方法是可调用的
# 类是可调用的
# 类的实例是可调用的
# 生成器是可调用的
