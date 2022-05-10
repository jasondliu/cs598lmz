import bz2
bz2.compress(b'hello')

#bz2.decompress(b'BZh91AY&SY\x94\x06\x00\x00\x00\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

import json
json.dumps([1, 2, 3, {'4': 5, '6': 7}])

json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

json.dumps(False)

json.dumps(42)

json.dumps(42, separators=(',', ':'))


obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)

import pickle
d = dict(name='Bob', age=20, score=88
