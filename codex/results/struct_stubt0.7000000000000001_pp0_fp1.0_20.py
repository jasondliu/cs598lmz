from _struct import Struct
s = Struct.__new__(Struct)
s.format = '&lt;hhl'
s.size = s.calcsize(s.format)
data = open(sys.argv[1], 'rb').read(s.size)
width,  height, image_size = s.unpack(data)
print width,  height, image_size
</code>

