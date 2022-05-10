import _struct
# Test _struct.Struct().
with self.assertRaises(ValueError):
  _struct.Struct('i')
with self.assertRaises(TypeError):
  _struct.Struct('i', None)
with self.assertRaises(TypeError):
  _struct.Struct('i', 0)
with self.assertRaises(TypeError):
  _struct.Struct('i', 1)
with self.assertRaises(TypeError):
  _struct.Struct('i', 'foo')
with self.assertRaises(TypeError):
  _struct.Struct('i', 'foo', None)
with self.assertRaises(TypeError):
  _struct.Struct('i', 'foo', 0)
with self.assertRaises(TypeError):
  _struct.Struct('i', 'foo', 1)
with self.assertRaises(TypeError):
  _struct.Struct('i', 'foo', 'bar')
with self.assertRaises(TypeError):
  _struct.Struct('i', 'foo', 'bar', None)
with self.assertRaises(TypeError):
  _struct.Struct
