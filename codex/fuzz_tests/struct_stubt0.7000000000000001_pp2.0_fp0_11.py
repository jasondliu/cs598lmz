from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__("format", "I")
s.size = 4
from _struct import pack, unpack
unpack("I", pack("I", 1))

from _struct import Struct
from itertools import repeat
from operator import mul
s = Struct.__new__(Struct)
s.__setattr__("format", "I" * int(reduce(mul, repeat(3, 3))))
s.size = 12
from _struct import pack, unpack
unpack("I", pack("I", 1))

from _struct import Struct
from itertools import repeat
from operator import mul
s = Struct.__new__(Struct)
s.__setattr__("format", "I" * int(reduce(mul, repeat(3, 3))))
s.size = 12
from _struct import pack, unpack
unpack("I" * int(reduce(mul, repeat(3, 3))), pack("I" * int(reduce(mul, repeat(3, 3))), 1, 2, 3))

from _struct import Struct
from
