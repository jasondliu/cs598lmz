import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1) / ctypes.c_int(0)
ctypes.pointer(S())
"""

import ctypes

data = 'Whats upppppppppppppppppp'


def main():
    lib_c = ctypes.CDLL("./build/libpyctypes_ex.so")
    c_buf_type = ctypes.c_char_p
    c_buf = c_buf_type(ctypes.create_string_buffer(data))
    lib_c.print_hello(c_buf_type(c_buf))

if __name__ == '__main__':
    main()
