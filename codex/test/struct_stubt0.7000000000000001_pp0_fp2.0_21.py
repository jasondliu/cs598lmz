from _struct import Struct
s = Struct.__new__(Struct)
s.format = '2sI'
s.size = s.calcsize(s.format)
s

# %%
s = Struct('2sI')
s.size

# %%
s = Struct('2sI')
s.unpack(b'AB\x00\x00\x00\x0d')

# %%
s = Struct('2sI')
s.unpack_from(b'AB\x00\x00\x00\x0d')

# %%
s = Struct('2sI')
s.unpack_from(b'AB\x00\x00\x00\x0d', 0)

# %%
s = Struct('2sI')
s.unpack_from(b'AB\x00\x00\x00\x0d', 1)

# %%
s = Struct('2sI')
s.unpack(b'AB\x00\x00\x00\x0d', 1)

# %%
s = Struct('2sI')
s.unpack_
