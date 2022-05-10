from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

compiled_s = Struct('I 2s f')
compiled_s.size


with open('data.b', 'rb') as f:
    data = f.read()

compiled_s.unpack(data)

# s.unpack(data)
# >>> error as s is not build as a compiled class yet

s = Struct('I 2s f')
s.unpack(data)
