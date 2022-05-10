import ctypes
# Test ctypes.CField.
class _EP(ctypes.Structure):
    _fields_ = [('name', ctypes.CField)]
    def __len__(self):
        return ctypes._calcsize(_EP, _EP._fields_)
assert _EP.name.offset == 0
assert _EP.name.size == 4
assert _EP.n_fields == 1
# Test ctypes.Padding.
class _M(ctypes.Structure):
    _fields_ = [('pad1', ctypes.Padding(4)), 
                ('name', ctypes.CField),
                ('pad2', ctypes.Padding(4))]
    def __len__(self):
        return ctypes._calcsize(_M, _M._fields_)
assert type(ctypes.CField) is ctypes._CField
assert type(ctypes.Padding) is ctypes._CField
assert _M.pad1.offset == 0
assert _M.pad1.size == 4
assert _M.name.offset == 4
assert _M.name.size == 4
assert _M
