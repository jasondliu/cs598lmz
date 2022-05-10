import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
def is_prime(n):
    if n &lt;= 1: 
        return 0
    if n == 2 or n == 3: 
        return 1
    if n % 2 == 0 or n % 3 == 0:
        return 0
    i = 5
    while i * i &lt;= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i = i + 6
    return 1

is_prime_c = FUNTYPE(is_prime)
so_file = ctypes.CDLL('./fib.so')
so_file.is_prime.argtypes = [ctypes.c_int]
so_file.is_prime.restype  = ctypes.c_int

for n in range(8):
    if so_file.is_prime(n) != is_prime(n):
        print(n)
</code>
Perhaps I can manually figure out where the problem is, but shouldn
