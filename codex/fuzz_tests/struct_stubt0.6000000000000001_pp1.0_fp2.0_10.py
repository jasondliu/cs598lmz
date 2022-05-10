from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i?f')
s.size

t = Struct('i?f')
t.size

import struct
rawsize = struct.calcsize('i?f')
rawsize

# %% [markdown]
# ### Packing and Unpacking

# %%
bin(386)

# %%
bin(386 & 0xffff)

# %%
bin(386 ^ 0xffff)

# %%
bin(386 | 0xffff)

# %%
bin(386 << 16)

# %%
bin(386 >> 16)

# %%
h = 0x82
m = 0x13
s = 0x17
b = (h << 16) | (m << 8) | s
b

# %%
bin(b)

# %%
bin(b & 0xff)

# %%
bin(b & 0xff00)

# %%
bin(b & 0xff0000)

# %%
bin(b & 0xff000000)

# %%
bin((b & 0xff000000) >> 24)

#
