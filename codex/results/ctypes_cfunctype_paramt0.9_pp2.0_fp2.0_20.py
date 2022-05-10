import ctypes
FUNTYPE = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p )  # function prototype
callback = FUNTYPE(ptx_decrypt)  # create function pointer
Protector.ptx_key_register_callback(callback)

status = Protector.ptx_key_setf(1,"k","\xff"*512)

if status == 0:
    print "OK"
if status < 0:
    print "Something went wrong"

status = Protector.ptx_key_gen()

if status == 0:
    print "Keys generated!"
if status < 0:
    print "Something went wrong"

status = Protector.ptx_session_start(1)

if status == 0:
    print "Session started!"
if status < 0:
    print "Something went wrong"

status = Protector.ptx_seal(1,1,"\xc0"*32)

if status == 0:
    print "Sealed!"
if status < 0:
    print "Something went
