from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('h')
s.size

# Python 2.6, 2.7
from _struct import Struct
s = Struct('h')
s.size
</code>

