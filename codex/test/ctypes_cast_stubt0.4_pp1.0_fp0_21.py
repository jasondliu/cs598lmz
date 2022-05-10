import ctypes
ctypes.cast(0, ctypes.py_object)

# <codecell>

# Allocate a buffer to hold the bytes
# Note that the buffer is not initialized
buf = ctypes.create_string_buffer(10)
buf.raw

# <codecell>

# Initialize the buffer
