from _struct import Struct
s = Struct.__new__(Struct)
f = s.format

if is_py2:
    buffer = memoryview
else:
    buffer = memoryview
    Struct.buffer_info = Struct.buffer_info
    def _struct_i(self):
        return self.format, self.size, self.alignment
    Struct.__reduce_ex__ = _struct_i

def _append_method(cls, name, func):
    m = getattr(cls, name, None)
    if m is not None:
        assert m.__func__ is func
        return
    # use setattr to avoid infinite recursion when we add method to Struct
    setattr(cls, name, func)

def _add_methods(cls):
    _append_method(cls, 'pack', _methods._pack)
    _append_method(cls, 'pack_into', _methods._pack_into)
    _append_method(cls, 'unpack', _methods._unpack)
