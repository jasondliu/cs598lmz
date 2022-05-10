import select
# Test select.select
# return value is a tuple with 3 elements
# 1st: bool indicates if the file is ready for read
# 2nd: bool indicates if the file is ready for write
# 3rd: bool indicates if there's an error
print(select.select((sys.stdin,
                     sys.stdout),
                    (sys.stdin,
                     sys.stdout),
                    (sys.stderr,
                     sys.stderr)))

print(sys.stdout.fileno())

# see: https://docs.python.org/3/library/select.html
# Note that Unix file descriptors can be used as a C int data type, which is not necessarily the same size as an int Python object used
# by the struct module. It is also possible to use long integers if they are available in your C implementation.
# It’s best to use the select() function with the smallest integer objects that will fit the system’s file descriptor type.

import struct
import os
