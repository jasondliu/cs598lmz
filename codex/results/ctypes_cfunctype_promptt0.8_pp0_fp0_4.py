import ctypes
# Test ctypes.CFUNCTYPE with use of ctypes.c_int
from ctypes import * 
libc = cdll.msvcrt 
printf = libc.printf
printf("Hello, world!\n")
printf("number: %d\n", 123) 
printf(b"number: %d\n", 123) 
printf("floating point number: %f\n", 0.5) 
printf("floating point number: %4.2f\n", 0.5) 
printf("%s\n", b"Hello, world!\n") 
printf("char: %c\n", b"a"[0]) 
printf("hex number: %x\n", 0x1234) 
printf("hex number: %X\n", 0x1234)

buffer = c_buffer(32) 
printf("address: %p\n", buffer) 
printf("string: %s\n", buffer)

libc.sprintf(buffer, b"%s, %s!\n", b"Hello", b"world") 
print(buffer.value)
#
