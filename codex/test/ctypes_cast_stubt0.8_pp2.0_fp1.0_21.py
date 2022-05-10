import ctypes
ctypes.cast(id(0), ctypes.py_object).value


def func():
    print("func")
    return "返回值"


var = func   # 变量指向函数
var()        # 变量调用函数
func()       # 函数本身调用


# 可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    print(total)


add()
add(1)
add(1, 2)
add(1, 2, 3)


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

