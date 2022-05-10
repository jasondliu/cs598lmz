import types
types.FunctionType

L = list(filter(lambda x: x%2==1, range(1,20)))
print(L)

def is_odd(n):
    return n%2==1

L = list(filter(is_odd, range(1,20)))
print(L)

# 把一个序列中的空字符串删除掉
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# 用filter求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(
