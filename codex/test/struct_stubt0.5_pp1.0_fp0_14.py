from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('=I')
s

# In[ ]:

s.pack(1)


# In[ ]:

s.pack(0xffffffff)


# In[ ]:

s.pack(0x12345678)


# In[ ]:

s.pack(0x1234)


# In[ ]:

s.pack(0x5678)


# In[ ]:

s.pack(0x56781234)


# In[ ]:

s.pack(0x34127856)


# In[ ]:

s.unpack(b'\x12\x34\x56\x78')


# In[ ]:

s.unpack(b'\x78\x56\x34\x12')


# In[ ]:

import time
time.time()


# In[ ]:

time.gmtime()


# In[ ]:

