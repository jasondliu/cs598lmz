import types
# Test types.FunctionType and types.LambdaType
def fibonacci_recursive(x):
    if x <= 1:
        return x
    else:
        return fibonacci_recursive(x - 1) + fibonacci_recursive(x - 2)


def fibonacci_tail_recursive(x, tail_recursion=False, n=0, f_n=0, f_nplus1=1):
    if x <= 1:
        return x
    if tail_recursion:
        return fibonacci_tail_recursive(x - 1, True, n + 1, f_nplus1, f_n + f_nplus1)
    else:
        return fibonacci_tail_recursive(x - 1, False, n + 1, f_nplus1, f_n + f_nplus1)


def fibonacci_while_loop(x):
    fib_n, fib_nplus1 = 0, 1
    while x > 0:
        fib_n, fib_nplus1 = fib_nplus1, fib_n + fib
