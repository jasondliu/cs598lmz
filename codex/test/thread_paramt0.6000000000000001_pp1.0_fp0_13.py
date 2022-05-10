import sys, threading
threading.Thread(target=lambda: sys.stdout.write("hello\n")).start()
threading.Thread(target=lambda: sys.stdout.write("world\n")).start()

# 3. 闭包
# 闭包 = 函数 + 环境变量（函数定义时的环境）
def multiply(x):
    def times(y):
        return x * y
    return times

double = multiply(2)
triple = multiply(3)
print(double(4))
print(triple(4))

# 4. 偏函数
def add(x, y):
    return x + y

from functools import partial
add_5 = partial(add, 5)
print(add_5(2))

# 5. 字符串格式化
template = "{0} love {1}"
print(template.format("I", "you"))

# 6. 字符
