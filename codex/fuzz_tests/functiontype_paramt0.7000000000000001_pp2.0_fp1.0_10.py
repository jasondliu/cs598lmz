from types import FunctionType
list(FunctionType(lambda: None).__code__.co_freevars)

# 匿名函数的属性不能通过点号来访问，因为匿名函数没有名字
# 匿名函数的属性也可以通过__dict__函数来访问
# 查看匿名函数的属性，可以通过几种方式：
# 1.可以使用getattr函数来访问
# 2.使用inspect.getmembers函数
# 可以看到，匿名函数中没有name属性
from inspect import getmembers
getmembers(lambda: None)
# 可以
