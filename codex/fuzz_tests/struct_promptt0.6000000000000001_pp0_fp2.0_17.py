import _struct
# Test _struct.Struct.__reduce__
s = _struct.Struct('<12s')
s.__reduce__()
s = _struct.Struct('12s')
s.__reduce__()
s = _struct.Struct('<12s')
s.__reduce__()
s = _struct.Struct('12s')
s.__reduce__()
s = _struct.Struct('<12s')
s.__reduce__()
s = _struct.Struct('12s')
s.__reduce__()
# Test _struct.Struct.__reduce_ex__
s = _struct.Struct('<12s')
s.__reduce_ex__(0)
s = _struct.Struct('12s')
s.__reduce_ex__(1)
s = _struct.Struct('<12s')
s.__reduce_ex__(2)
s = _struct.Struct('12s')
s.__reduce_ex__(3)
s = _struct.Struct('<12s')
s.__reduce_ex__(4)
s
