import bz2
bz2.decompress(compressed_data)

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

import json
json.dumps([1, 'simple', 'list'])

x = json.dumps(['simple', 'list'])
x

json.loads(x)

json.dumps(('complex', 'tuple'))

json.dumps(1+2j)

json.dumps(set([1, 2, 3]))

json.dumps({'Name': 'Zara', 'Age': 7, 'Class': 'First'})

json.dumps(('e', {'x': ('y', None, 1.0, 2)}))

json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)

from io import StringIO
io = StringIO()
json
