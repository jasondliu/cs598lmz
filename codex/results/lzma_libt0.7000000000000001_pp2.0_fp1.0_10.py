import lzma
lzma.decompress(m)

# Now what?

m

# Bytes are just numbers.
# Treat them as such.

unhexlify('666f6f626172')

# We can use the mathematical conversion for Base64
# to convert between Base64 and bytes.

import base64
base64.b64decode(b'Zm9vYmFy')

# Note that base64.b64decode()
# returns bytes.
#
# To convert it into a string,
# we need to decode it.
#
# Encoding is a mathematical conversion
# from bytes to a string.

base64.b64decode(b'Zm9vYmFy').decode()

# The reverse mathematical conversion is called decoding.
#
# Note that base64.b64encode()
# expects a bytes object.
#
# To convert a string into bytes,
# we need to encode it.

base64.b64encode(b'foobar')


# In[ ]:


# Suppose we want to see the
