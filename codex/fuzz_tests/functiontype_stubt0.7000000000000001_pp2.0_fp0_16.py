from types import FunctionType
a = (x for x in [1])
type(a)

from types import GeneratorType
a = (x for x in [1])
print(type(a))

#查看函数的参数
def chk_param(fn):
    def wrapper(*args, **kwargs):
        if isinstance(fn, FunctionType):
            print(fn.__name__)
            for a in args:
                print(a)
            for a in kwargs.items():
                print(a)
        return fn(*args, **kwargs)

    return wrapper


@chk_param
def add(x, y=8):
    return x + y

print(add(3,y=7))

#堆栈打印
import inspect
inspect.stack()

#查看类的继承关系
print(Person.__bases__)
print(Student.__bases__)
print(Student.__mro__)

#查看类的
