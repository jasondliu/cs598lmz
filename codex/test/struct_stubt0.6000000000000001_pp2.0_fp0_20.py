from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i', 4)
s.size

s.pack(1)

s.unpack(b'\x00\x00\x00\x01')

s.unpack(b'\x01\x00\x00\x00')

s.unpack_from(b'\xff\x00\x00\x00\x00\x00\x00\x01')

s.unpack_from(b'\x00\x00\x00\x01\x00\x00\x00\x02', 4)


# ## Struct as a context manager
# 
# The `Struct` class also supports the context manager protocol.
# When used in a `with` statement, it automatically calls the `pack`
# and `unpack` methods, as appropriate.

# In[12]:


from _struct import Struct
with Struct('>i') as s:
    b = s.pack(1)
    print(b)
    print(s.unpack(b))


# ## Byte order,
