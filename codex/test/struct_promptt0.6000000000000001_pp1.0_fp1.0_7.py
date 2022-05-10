import _struct
# Test _struct.Struct.
if sys.platform == 'win32':
  # Windows doesn't support the Q format
  print(_struct.Struct('Q').size)
  s = _struct.Struct('Q')
  print(s.pack(123456789012345))
  print(s.pack(123456789012345678901234567890))
  print(s.unpack(b'\x12\x34\x56\x78\x9a\xbc\xde\xf1'))
  print(s.unpack(b'\x12\x34\x56\x78\x9a\xbc\xde\xf1\x23\x45\x67\x89\xab\xcd\xef\x01'))
else:
  print(_struct.Struct('Q').size)
  s = _struct.Struct('Q')
  print(s.pack(123456789012345))
