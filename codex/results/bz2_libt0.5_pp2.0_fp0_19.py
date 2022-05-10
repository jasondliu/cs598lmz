import bz2
bz2.decompress(bz2_data)

# #### Hexadecimal
# 
# The `binascii` module contains a number of methods for converting between binary and various ASCII-encoded binary representations. `hexlify` and `unhexlify` are particularly useful for dealing with hexadecimal representations of binary data.

# In[ ]:


import binascii

hex_data = binascii.hexlify(b'binary\x00string')
print(hex_data)

binascii.unhexlify(hex_data)


# ## Structured Data: NumPy and Pandas
# 
# While built-in Python containers can be useful, they tend to be somewhat slow in practice due to their flexibility. For example, they are dynamically typed and hence require type checking at runtime.
# 
# This section will introduce the `NumPy` and `Pandas` libraries, which provide efficient storage and manipulation for dense or sparse arrays.
# 
# ### NumPy Basics
# 
# The `NumPy` package (pronounced as "Num-pee
