from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('4s', '')
</code>
There is no <code>_struct.Struct()</code> constructor in Python, there is only <code>_struct.Struct.__new__(Struct, ...)</code> constructor.
The following code works without error:
<code>#!/usr/bin/env python
from _struct import Struct

s = Struct.__new__(Struct)
s.__init__('4s', '')

print(s)
</code>

