from types import FunctionType
a = (x for x in [1])
a(3)


# @lru_cache(maxsize=1000)
# def fibonacci(n):
#     if n < 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# fibonacci(1000)
# fibonacci.cache_info()
# print(fibonacci.cache_info())
# print(fibonacci.cache_info())
# print(fibonacci.cache_info())


# import random

# @lru_cache(maxsize=32)
# def randint(lower, upper):
#     return random.randint(lower, upper)
# print(randint(1, 10))

# randint.cache_info()
