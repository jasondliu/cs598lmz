import _struct

__all__ = ['c_int64', 'c_uint64', 'c_longlong', 'c_ulonglong']

c_int64 = _struct.Struct('q')
c_uint64 = _struct.Struct('Q')
c_longlong = c_int64
c_ulonglong = c_uint64
