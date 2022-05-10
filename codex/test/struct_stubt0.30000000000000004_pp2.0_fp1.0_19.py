from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 函数可以被赋值给变量，变量可以作为函数的参数
def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)

def print_result(result):
    print('Got:', result)

def add(x, y):
    return x + y

apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)

# 函数也可以作为闭包
def make_closure(a):
    def closure():
        print('I know the secret: %d' % a)
    return closure

closure = make_closure(5)
closure()

#
