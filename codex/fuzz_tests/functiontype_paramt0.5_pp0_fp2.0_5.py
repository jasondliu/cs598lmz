from types import FunctionType
list(FunctionType(lambda x:x+1, {}).__globals__.items())

# 下面是一个更加复杂的例子
# 下面的例子中，嵌套的函数使用了外部函数的变量，并且返回了内部函数的引用
def sample():
    n = 0
    # Closure function
    def func():
        print('n=', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func

f = sample()
f()
f.set_n(10)
f()
print(f.get_n())

# 下面
