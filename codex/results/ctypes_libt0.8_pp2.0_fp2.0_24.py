import ctypes
ctypes.cdll.LoadLibrary("libc.so.6")
libc = ctypes.CDLL("libc.so.6")

libc.system("id")


libc.printf("%s\n", "Hello world!")
