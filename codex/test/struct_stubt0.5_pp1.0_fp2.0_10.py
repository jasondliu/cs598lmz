from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(3)

# Example 3-2. Using the Struct constructor to create a new Struct instance
from _struct import Struct
Struct('i')
Struct('i').pack(3)

# Example 3-3. The Struct class methods
from _struct import Struct
s = Struct('i')
s.pack(3)
s.unpack(_)
s.unpack_from(_, 0)
s.iter_unpack(_)
s.size
s.format

# Example 3-4. Struct format strings
from _struct import Struct
Struct('x')
Struct('i')
Struct('f')
Struct('s')

# Example 3-5. Struct format string modifiers
from _struct import Struct
Struct('i')
Struct('iP')
Struct('iP3s')
Struct('i5s')
Struct('i5sh')
Struct('i5sh10s')
Struct('i5sh10sf')

# Example 3-6. Struct format string modifiers
from _struct import Struct
Struct('i')
