import lzma
lzma.LZMAError

d = [(1, 2), (3, 4), (5, 6)]
for i, (a, b) in enumerate(d):   print(i, a, b)


for i, (a, b) in enumerate(d):
print(i, a, b)

i, a, b

l = [1, 2, 3]
l = (1, 2, 3)
l = {1, 2, 3}
l = {'a': 1, 'b': 2}
l = {1: 'a', 2: 'b'}

c = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c.items()

import collections
collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])

def find_max(a):
    m = a[0]
    for i in a:
        if i > m:
            m = i
    return m


def find_max(a):
    m = a[
