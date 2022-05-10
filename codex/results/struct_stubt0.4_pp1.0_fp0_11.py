from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x00\x00\x00\x00')

# Disassembly of _struct.Struct.__new__
# 4           0 LOAD_GLOBAL              0 (Struct)
#             3 CALL_FUNCTION            0
#             6 RETURN_VALUE

# Disassembly of _struct.Struct.__init__
# 4           0 LOAD_FAST                0 (self)
#             3 LOAD_ATTR                1 (format)
#             6 LOAD_FAST                1 (format)
#             9 CALL_FUNCTION            1
#            12 STORE_ATTR               1 (format)
#            15 LOAD_CONST               0 (None)
#            18 RETURN_VALUE

# Disassembly of _struct.Struct.unpack
# 4           0 LOAD_FAST                0 (self)
#             3 LOAD_ATTR                1 (format)
#             6 LOAD_FAST                1 (data)
#             9 CALL_FUNCTION            2
#            12 RET
