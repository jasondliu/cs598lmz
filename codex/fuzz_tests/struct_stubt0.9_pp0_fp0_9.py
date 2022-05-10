from _struct import Struct
s = Struct.__new__(Struct)
print(type(s), 'using _struct.Struct')

from _namedtuple import namedtuple
n = namedtuple.__new__(namedtuple, "count", "a b c")
print(type(n), 'using _namedtuple.namedtuple')

from _datetime import datetime
# Assembled a datetime object manually
# Apparently, a classmethod constructor is used to set attributes
d = datetime.__new__(datetime, 0, 0, 0, 0, 0, 0, 0, 0, 8)
print(type(d), 'using _datetime.datetime')

from _deque import deque
q = deque.__new__(deque, (1,))
q.maxlen = 0
q.pop = deque.pop
print(type(q), 'using _deque.deque')

from _collections import ChainMap
c = ChainMap.__new__(ChainMap, {}, {})
print(type(c), 'using _collections.ChainMap')

from _blake2 import blake
