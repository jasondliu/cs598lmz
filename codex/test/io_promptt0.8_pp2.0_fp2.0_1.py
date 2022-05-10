import io
# Test io.RawIOBase, Issue 13238
# Use the following sequence of bytes:
# b'0123456789abcdef'
# Treat this as little-endian
# Read in 1 byte (8 bits) at a time.
# The first time, return -1 to indicate EOF.
# Next, return 8 bits (1 byte) in each call.
# Then return 16 bits (2 bytes) in each call.
# Then return 24 bits (3 bytes) in each call.
# Then return 32 bits (4 bytes) in each call.
# Then return 40 bits (5 bytes) in each call.
# Then return 48 bits (6 bytes) in each call.
# Then return 56 bits (7 bytes) in each call.
# Finally, return 64 bits (8 bytes) in each call.
# Then return 64 bits (8 bytes) in each call.
# Then return 64 bits (8 bytes) in each call.
# Then return 64 bits (8 bytes) in each call.
# Then return 64 bits (8 bytes) in each call.
# Then return 8 bits (1 byte) in each call.
# After that, return EOF again
