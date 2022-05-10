from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

import io
from struct import Struct
s = Struct('i')
s.size

from struct import Struct
s = Struct('i')
s.size

from struct import Struct
Struct.__new__(Struct, 'i').size

from struct import Struct
s = Struct('i')
s.__new__(s)

from struct import Struct
Struct.__new__(Struct, 'i').__new__(Struct, 'i')

from struct import Struct
s = Struct('i')
s.__init__('i')

from struct import Struct
s = Struct('i')
s.__init__('I')

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I')

from struct import Struct
s = Struct('i')
s.format

from struct import Struct
s = Struct('i')
s.format_char

from
