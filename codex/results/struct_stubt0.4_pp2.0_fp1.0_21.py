from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I 2s f'
s.size = s.calcsize()

print(s.size)
print(s.pack(1,b'ab',2.7))

# 可以用 OrderedDict 保证键的顺序
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key,d[key])

import json
print(json.dumps(d))

# 实现一个 FIFO（先进先出）的 dict，当容量超出限制时，先删除最早添加的Key
from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(
