import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)
lib = ctypes.CDLL('libc.so.6')
lib.printf("Hello %s\n","World")
lib.printf("Hello %s\n",b"World")
lib.printf("Hello %s\n",b"World".decode())
lib.printf("Hello %s\n","World".encode())
lib.printf("Hello %s\n",u"World")

lib.printf("Hello %s\n",1)

lib.printf("Hello %s\n",1.0)

lib.printf("Hello %s\n",1+0j)

lib.printf("Hello %s\n",[1,2,3])

lib.printf("Hello %s\n",b"World")

lib.printf("Hello %s\n",bytearray(b"World"))

lib.printf("Hello %s\n",memoryview(b"World"))

lib.printf("Hello %s\n",(1,2,3))

lib.printf("Hello
