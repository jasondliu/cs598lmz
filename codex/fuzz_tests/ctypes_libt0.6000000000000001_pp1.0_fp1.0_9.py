import ctypes
ctypes.CDLL('./my_lib.so', ctypes.RTLD_GLOBAL)

import my_lib
my_lib.my_function()
</code>

