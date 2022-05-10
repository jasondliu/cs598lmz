from types import FunctionType
list(FunctionType(lambda x,y:x+y,globals(),'__add__')(1,2))

# 创建匿名函数lambda
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# lambda x: x + 1
# 匿名函数有个限制，就是只能有一个表达式，不用写return，
# 返回值就是该表达式的结果。
# lambda x: x * x可以写成匿名函数
# lambda x: x * x
# 匿名函数也是一个函数对象，也可以把
