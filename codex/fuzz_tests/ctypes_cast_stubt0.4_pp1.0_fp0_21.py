import ctypes
ctypes.cast(0, ctypes.py_object)

# <codecell>

# Allocate a buffer to hold the bytes
# Note that the buffer is not initialized
buf = ctypes.create_string_buffer(10)
buf.raw

# <codecell>

# Initialize the buffer
buf.value = 'Hello'
buf.raw

# <codecell>

# Set a byte
buf[0] = 'J'
buf.raw

# <codecell>

# Get a byte
buf[0]

# <codecell>

# Set a slice of bytes
buf[1:5] = 'ello'
buf.raw

# <codecell>

# Get a slice of bytes
buf[1:5]

# <codecell>

# Get a slice of bytes as a list
list(buf[1:5])

# <codecell>

# Get a slice of bytes as a list
list(buf)

# <codecell>

# Get a slice of bytes as a list
list(buf[:])

# <
