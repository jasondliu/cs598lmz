from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s

# In[ ]:

s.size


# In[ ]:

s.pack(1, b'ab', 2.7)


# In[ ]:

s.unpack(_)


# In[ ]:

s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x00@\x9a\x99\x99\x99\x99\x99\xf9?')


# In[ ]:

s.unpack_from(b'\x01\x00\x00\x00ab\x00\x00\x00@\x9a\x99\x99\x99\x99\x99\xf9?', 4)


# In[ ]:

import struct
struct.pack('>I', 10240099)


# In[ ]:

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80
