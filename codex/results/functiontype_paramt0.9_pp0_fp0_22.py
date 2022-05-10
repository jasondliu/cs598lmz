from types import FunctionType
list(FunctionType(f.__code__, globals(), 'random_func'))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
factorial = my_trace(factorial) # modify factorial
factorial(5) # prints result and is otherwise unchanged
 
# this shows how recursion is detected (i.e. how long the stack trace is):
factorial(5) # prints result and is otherwise unchanged


def mul(a=1):
    return a
def add(a=2):
    return a
def main():
    mul_return = mul()
    add_return = add(mul_return)
    return add_return

if __name__ == '__main__':
    print(main())
