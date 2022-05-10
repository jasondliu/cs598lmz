from types import FunctionType
list(FunctionType(lambda x: x+1, globals(), 'lambda_func') for x in range(10))

# 列表推导式
# 列表推导式是列表解析的语法糖
# 列表推导式是一种将for循环和if语句合并成一行的方式
# 列表推导式的返回值是一个列表
# 列表推导式的语法是在一个方括号内放置一个表达式，后面跟一个for循环，然后有零到多个for或if子句
# 列表推导式的
