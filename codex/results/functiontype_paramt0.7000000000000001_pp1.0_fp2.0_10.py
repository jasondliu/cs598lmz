from types import FunctionType
list(FunctionType(lambda: None, {}))  # [None]

# 函数使用 __closure__ 属性保存绑定在其上的环境变量。
def make_adder(augend):
    def adder(addend):
        return augend + addend
    return adder

a = make_adder(23)
a.__closure__[0].cell_contents  # 23

# 捕获外部变量通常用来创建闭包，闭包是一种函数对象，它会保留定义函数时存在的自由变量的绑定。
# 在函数中可以访问这个绑定，即使这个函数在
