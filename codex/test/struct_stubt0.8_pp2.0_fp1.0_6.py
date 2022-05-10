from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

s.pack(1)

s.unpack(_)

s.unpack_from(b'\x00\x00\x00\x01', 0)



# %%
from struct import Struct
st = Struct('>I')
st.size

st.pack(1)

st.unpack(_)

st.unpack_from(b'\x00\x00\x00\x01', 0)



# %%
from struct import pack
pack('>I', 1)



# %%
with open('myfile.zip', 'rb') as f:
    data = f.read()



# %%
import os
os.stat('myfile.zip').st_size

len(data)



# %%
from struct import unpack
unpack('I', data[:4])



# %%
unpack('>I', data[:4])

unpack('I', b'\x00\x00\x00\x01')


