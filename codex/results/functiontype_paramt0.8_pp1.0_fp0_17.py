from types import FunctionType
list(FunctionType("", globals()) for i in [1])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: generator already executing

# 生成器是可以暂停的函数，生成器函数一旦被调用并执行到第一个yield语句，它就会返回一个生成器对象。
# 只有当生成器对象被next()函数反复调用时，生成器才继续执行，yield语句可以产出值，也可以接收值

# first use generator
def gen_fib(
