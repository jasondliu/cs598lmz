from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# 方法二
from _struct import Struct
s = Struct('i')
s.size

# 方法三
from _struct import calcsize
calcsize('i')

# 方法四
import struct
struct.calcsize('i')

# 方法五
import struct
struct.Struct('i').size

# 方法六
import struct
struct.Struct('i').size

# 方法七
import struct
struct.Struct('i').size

# 方法八
import struct
struct.Struct('i').size

# 方法九
import struct
struct.Struct('i').size

# 方法十
import struct
struct.Struct('i').size

# 方法十一
import struct
struct.Struct('i').size

# 方法十二
import struct
struct.Struct('i').
