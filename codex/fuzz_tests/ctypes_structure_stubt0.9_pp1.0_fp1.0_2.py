import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
    i = ctypes.c_buffer(bytearray([0, 1, 2, 3]))

    _fields_ = [('a', ctypes.c_bool),
                ('b', ctypes.c_byte),
                ('c', ctypes.c_char),
                ('h', ctypes.c_short),
                ('i', ctypes.c_int),
                ('l', ctypes.c_long),
                ('q', ctypes.c_longlong),
                ('f', ctypes.c_float),
                ('d', ctypes.c_double),
                ('p', ctypes.c_void_p),
                ('s', ctypes.c_char_p),
                ]
print(S())

libc = ctypes.CDLL(None)

message_string = ctypes.create_string_buffer(32)
libc.sprintf(message_string, b"hello world")

print(message_string.value)
class POINT(ctypes.Structure):
    _fields
