from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.format
s.unpack(b'\x01\x02\x03\x04')
s.pack(1)
s.pack(1, 2, 3)


# In[ ]:


from _struct import Struct
s = Struct('i')
s.format
s.unpack(b'\x01\x02\x03\x04')
s.pack(1)
s.pack(1, 2, 3)


# In[ ]:


from _struct import Struct
s = Struct('i')
s.format
s.unpack(b'\x01\x02\x03\x04')
s.pack(1)
s.pack(1, 2, 3)
s.pack()


# In[ ]:


from _struct import Struct
s = Struct('i')
s.format
s.unpack(b'\x01\x02\x03\x04')
s.pack(1)
s.pack(1, 2, 3)
s.pack()

