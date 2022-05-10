import _struct
# Test _struct.Struct()
def test_struct():
  import _struct
  assert _struct.Struct('x')
  assert _struct.Struct('<x')
  assert _struct.Struct('<b')
  assert _struct.Struct('<b').size == 1
  assert _struct.Struct('<h').size == 2
  assert _struct.Struct('<i').size == 4
  assert _struct.Struct('<l').size == 4
  assert _struct.Struct('<q').size == 8
  assert _struct.Struct('<f').size == 4
  assert _struct.Struct('<d').size == 8
  assert _struct.Struct('<x').size == 1
  assert _struct.Struct('<b').pack(0) == b'\x00'
  assert _struct.Struct('<b').pack(127) == b'\x7f'
  assert _struct.Struct('<b').pack(-128) == b'\x80'
  assert _struct.Struct('<h').pack(0) == b'\x00\x00'
  assert _struct.Struct('
