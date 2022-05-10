from _struct import Struct
s = Struct.__new__(Struct)

# Set the format
s.format = '&gt;I'

# Get the size
s.size = s.calcsize()

# Set the unpacked data
s.data = [0x42]

# Get the packed data
packed = s.pack(*s.data)
</code>
Is there a better way to do this?

