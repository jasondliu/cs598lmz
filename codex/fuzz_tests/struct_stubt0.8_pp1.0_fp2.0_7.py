from _struct import Struct
s = Struct.__new__(Struct)
with open("data.bin", "rb") as f:
    s.buffer_info = (f.read(),0)
    print (s.unpack("&lt;5I"))
</code>

