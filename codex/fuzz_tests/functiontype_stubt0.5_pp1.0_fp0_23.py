from types import FunctionType
a = (x for x in [1])
type(a)

# 函数对象有一个__name__属性，可以拿到函数的名字
def now():
    print('2015-3-25')
f = now
print(f.__name__)

# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上
