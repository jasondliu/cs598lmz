import bz2
# Test BZ2Decompressor

cmpobj = bz2.BZ2Decompressor()
decompressed_data = []
for chunk in iter(lambda: f.read(100 * 1024), b''):
    decompressed_data.append(cmpobj.decompress(chunk))

decompressed_data
from itertools import repeat
list(map(list, zip(repeat(1), [2, 3, 4])))
 
from itertools import chain, repeat
def grouper(iterable, n, fillvalue=None):
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

list(grouper([1,2,3,4], 2))
from itertools import zip_longest
# Function that flattens out lists
def flatten(l): return flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else []) if type(l) is list else [l]


