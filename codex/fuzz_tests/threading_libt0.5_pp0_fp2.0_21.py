import threading
threading.stack_size(2**27)

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1)+f(n-2)

def print_fib(n):
    print('fib of', n, '=', f(n))

start = time.time()

print_fib(35)

print('time:', time.time()-start)

# print('fib of', 35, '=', f(35))
# print('time:', time.time()-start)

# import time
# start = time.time()
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
#
# print(f(35))
# print('time:', time.time()-start)
