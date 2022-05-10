import _struct
# Test _struct.Struct
_struct.Struct('i').pack(42)
"""
    self.do_run(src, '42')

  def test_struct_unpack(self):
    src = r"""
import _struct
# Test _struct.Struct
_struct.Struct('i').unpack(_struct.Struct('i').pack(42))
"""
    self.do_run(src, '42')

  def test_struct_unpack_from(self):
    src = r"""
import _struct
# Test _struct.Struct
_struct.Struct('i').unpack_from(_struct.Struct('i').pack(42), 0)
"""
    self.do_run(src, '42')

  def test_struct_iter_unpack(self):
    src = r"""
import _struct
# Test _struct.Struct
list(_struct.Struct('i').iter_unpack(_struct.Struct('i').pack(42)))
"""
    self.do_run(src, '42')

  def test_struct_calcsize(self):
    src = r"""
import _struct
