from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')
s.size

# 如果要调用实例方法，那么必须要给实例传入参数，否则会报错
# TypeError: __init__() missing 1 required positional argument: 'format'
s.unpack(b'\x12\x34')

# 如果要调用类方法，那么可以不用传入参数
Struct.unpack_from(b'\x12\x34')

# 如果要调用静态方法，那么也可以不用传入参数
Struct.iter_unpack(b'\x12\x34\x56\x78')
