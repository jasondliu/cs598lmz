from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(obj.data)

# %%
import pickle
pickle.loads(obj.data)

# %%
obj.data.decode("utf-8")

# %%
import struct
struct.unpack("<i", obj.data[:4])

# %%
obj.data[4:]

# %%
obj = pickle.loads(obj.data[4:])
obj

# %%
obj.data

# %%
struct.unpack("<i", obj.data[:4])

# %%
obj.data[4:]

# %%
obj = pickle.loads(obj.data[4:])
obj

# %%
obj.data

# %%
struct.unpack("<i", obj.data[:4])

# %%
obj.data[4:]

# %%
obj = pickle.loads(obj.data[4:])
obj

# %%
obj.data

# %%
struct.unpack("<i", obj.data[:4])

# %%
obj.data[4
