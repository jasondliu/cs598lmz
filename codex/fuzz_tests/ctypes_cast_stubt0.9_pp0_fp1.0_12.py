import ctypes
ctypes.cast(lib.AAA, ctypes.POINTER(ctypes.c_char)).contents.value
#> 'hello'
ctypes.POINTER(ctypes.c_char).from_buffer(lib.AAA).value
#> 'hello'
bytes(ctypes.addressof(lib.AAA))
#> b"hello"
ctypes.c_char.from_address(lib.AA).value
#> 'l'
ctypes.c_char.from_address(lib.AAA).value
#> 'h'
ctypes.c_char.from_address(lib.AAA + 1).value
#> 'e'
ctypes.c_char.from_address(lib.AAA + 2).value
#> 'l'
ctypes.c_char.from_address(lib.AAA + 3).value
#> 'l'
ctypes.c_char.from_address(lib.AAA + 4).value
#> 'o'
ctypes.c_char.from_address(lib.AAA + 5).value
#> '\x00'
ctypes.c
