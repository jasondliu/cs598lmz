from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(file_content)

# bz2.open
from bz2 import open
open('file.txt.bz2').read()

# pprint.pprint
from pprint import pprint
pprint(obj)

# itertools.combinations
from itertools import combinations
for c in combinations(iterable, r):
    print c

# itertools.permutations
from itertools import permutations
for c in permutations(iterable, r):
    print c

# itertools.product
from itertools import product
for c in product(iterable, r):
    print c

# itertools.count
from itertools import count
for i in count(start=10, step=-1):
    print i
    if i == 0:
        break

# itertools.accumulate
from itertools import accumulate
for i in accumulate(iterable, func=lambda x, y: x+y):
    print i

# itertools.islice
from itertools import islice
for
