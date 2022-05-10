from _struct import Struct
s = Struct.__new__(Struct)
s.defaults = (1, 'hello')
data = s.pack(2, 'world')
print(data)
print(s.unpack(data))
''' return >>>
@…\x00\x00\x00world
(2, 'world')
'''
from collections import defaultdict
def default_factory():
    return 'default value'
d = defaultdict(default_factory, foo='bar')
print(d['foo']) 
''' return >>>
bar
'''
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['b'].append(2)
print(d)
''' return >>>
defaultdict(list, {'a': [1], 'b': [2]})
'''
from collections import OrderedDict
from collections import Counter

class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'
    def __setitem__(self, key, value):
        if key in self:
            del self
