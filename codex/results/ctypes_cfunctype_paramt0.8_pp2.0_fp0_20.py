import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
f = FUNTYPE(lambda x: 3*x)
print(f)
print(f(2))

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# print_primes_func = FUNTYPE(lambda x: print(primes[x]))
# print_primes_func(3)

print_primes_func = FUNTYPE(lambda x: print(x))
print_primes_func(3)
print(print_primes_func)
print(print_primes_func.restype)
print(print_primes_func.argtypes)
print_primes_func.argtypes = [ctypes.c_int]
print(print_primes_func.argtypes)
print(print_primes_func.argtypes[0](3))

print_primes_func = FUNTYPE
