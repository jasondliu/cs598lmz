import mmap
# Test mmap.mmap exists
import mmap

# Test we can use 
import mmap

# Map the whole file, draw a rectangle
f = open("/dev/graphics/fb0", "r+")
m = mmap.mmap(f.fileno(), 0)

m[0x00] = chr(255)
m[0x01] = chr(255)
m[0x02] = chr(255)
m[0x03] = chr(255)
m[0x04] = chr(255)
m[0x05] = chr(255)
m[0x06] = chr(255)
m[0x07] = chr(255)
m[0x08] = chr(255)
m[0x09] = chr(255)
m[0x0a] = chr(255)
m[0x0b] = chr(255)
m[0x0c] = chr(255)
