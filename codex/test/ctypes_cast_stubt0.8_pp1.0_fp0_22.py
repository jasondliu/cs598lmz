import ctypes
ctypes.cast(0, ctypes.py_object)

# 函数返回值
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print(calc_sum(1,2,3,4))
print(calc_sum(1,2,3,4,5,6,7,8))

# 如果你已经把一个list或tuple传进来，要调用一个可变参数怎么办？可以这样做：
num = [1, 2, 3, 4, 5, 6]
calc_sum(*num)

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person
