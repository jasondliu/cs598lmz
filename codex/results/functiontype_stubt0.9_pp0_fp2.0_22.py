from types import FunctionType
a = (x for x in [1])

b = [1]
del b
# 局部变量的生命周期依赖于函数的执行时长
# 全局变量的引用计数组去5后还不为0, 则不被销毁

# 延迟变量的赋值会报UnboundLocalError
x = True
def test_global_var():
    print(x)
    x = False
try:
    print(x)
    test_global_var()
except UnboundLocalError:
    print('unbound local error')

# 可以通过global和nonlocal语句对全局和局部变量进行赋值

# python中变量声明前并不
