fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi # override __code__ with generator
# fn() # error: __code__ is not callable


# 2.5
def f(m):
    n = 0
    while n < m:
        n += 1
        if n % 5 == 0:
            return n
        yield n

# f(5) # <generator object f at 0x10b8a06a0>
# next(f(5)) # 1
# next(f(5)) # 2
# next(f(5)) # 3
# next(f(5)) # 4
# next(f(5)) # 5
# print(list(f(20))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
res = f(20)
# print(list(res)) # [1, 2, 3, 4, 5]
# print(list(res)) # [6, 7, 8, 9, 10]
# print(list(res)) # [11, 12
