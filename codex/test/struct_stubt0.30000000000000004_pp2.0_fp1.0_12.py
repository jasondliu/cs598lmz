from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# %%
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# %%
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# %%
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# %%
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)
s.unpack(b'\x00\x00\x00\x01')

# %%
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)
s.unpack(b'\x00\x00\x00\x01')

# %%
