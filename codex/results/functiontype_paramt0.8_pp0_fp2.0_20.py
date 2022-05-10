from types import FunctionType
list(FunctionType(square.__code__, {}, 'a'))

from operator import methodcaller
list(map(methodcaller('replace', 'o', '0'), 'hello'))

list(map(methodcaller('replace', 'o', '0'), ['hello']*10))

from functools import partial
from operator import mul
list(map(partial(mul, 2), range(10)))

from functools import lru_cache
from time import time

@lru_cache(maxsize=128)
def fib(n):
	if n < 2:
		return n
	return fib(n-2) + fib(n-1)

for i in range(10):
	print(i, ':', fib(i))

print('-'*60)

start = time()
for i in range(1000):
	fib(i)
duration = time() - start
print("Took %.3f seconds" % (duration,))
