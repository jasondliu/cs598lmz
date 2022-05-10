import types
# Test types.FunctionType
def make_adder(addend):
    def adder(augend):
        return augend + addend
    return adder
x = make_adder(2)
y = make_adder(4)
##x(3)
##y(5)

def do_twice(func):
    return func(func)

def print_spam():
    print('spam')
x = do_twice(print_spam)
print(x)

def do_four(func):
    do_twice(func)
    do_twice(func)

do_four(print_spam)

##do_twice(print_spam)

# Test types.LambdaType
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
##f(0)
##f(1)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
##pairs.sort(key=lambda pair
