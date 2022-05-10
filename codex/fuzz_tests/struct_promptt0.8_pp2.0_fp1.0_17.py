import _struct
# Test _struct.Struct constructors
s = _struct.Struct('i')   # native byte order
S = _struct.Struct('@i')  # native byte order
I = _struct.Struct('>i')  # big-endian
i = _struct.Struct('<i')  # little-endian

# Test _struct.Struct.size
if s.size != S.size != i.size != I.size != 4:
    print('_struct.Struct.size failed, s.size %d, S.size %d, i.size %d, I.size %d' % (s.size, S.size, i.size, I.size))

# Test various packing with 'i'
for fmt, data in [('i', 0),
                  ('i', 1),
                  ('i', 32767),
                  ('i', 32768),
                  ('i', 65535),
                  ('i', 65536),
                  ('i', (1<<31)-1),
                  ('i', -1),
                  ('i', -32768),
                  ('i', -32769),
                  ('i', -
