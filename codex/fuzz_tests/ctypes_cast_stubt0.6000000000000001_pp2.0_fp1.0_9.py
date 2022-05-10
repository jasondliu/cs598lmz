import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# def is_prime(num):
#     """
#     Better method of checking for primes. 
#     """
#     if num == 2:
#         return True
#     if num < 2 or num % 2 == 0:
#         return False
#     for n in xrange(3, int(num**0.5)+2, 2):
#         if num % n == 0:
#             return False
#     return True

# def get_primes(n):
#     """
#     Returns  a list of primes < n
#     """
#     sieve = [True] * n
#     for i in xrange(3,int(n**0.5)+1,2):
#         if sieve[i]:
#             sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
#     return [2] + [i for i in xrange(3,n,2) if sieve[i]]


