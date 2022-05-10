import bz2
bz2.decompress(bz2.compress(b'Hello World'))

a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]
c = [3, 4, 5, 6, 7]
d = [4, 5, 6, 7, 8]
import itertools
for aa in itertools.chain(a,b,c,d):
    print(aa)

aa = [a, b, c, d]
for aaa in itertools.chain.from_iterable(aa):
    print(aaa)

result = itertools.chain.from_iterable(aa)

for x in result:
    print(x)

import itertools
for x in itertools.accumulate(a):
    print(x)

import itertools
for x in itertools.accumulate(a, lambda x, y: x+y):
    print(x)

import itertools
for x in itertools.accumulate(a, lambda x
