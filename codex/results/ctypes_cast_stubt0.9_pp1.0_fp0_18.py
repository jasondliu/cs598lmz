import ctypes
ctypes.cast(h_buf, ctypes.POINTER(ctypes.c_ushort))[0]

opcode = "0000"
string_in = "example".encode('utf-8')
string_in = "000000330000007600000003".encode('utf-8')
# This is currently 0x20 buffer size
h_buf = clib.comm_put(len(string_in),string_in)
b_buf = ctypes.cast(h_buf, ctypes.POINTER(ctypes.c_char * len(string_in)))[0]
resp = b_buf.raw
t_end = time.time() + timeout
while (time.time() < t_end):
    if (resp != "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"):
        ctypes.cast(h_buf, ctypes.POINTER(ctypes.c_ushort))[0]
        print(resp)
        break
    time.sleep(0.001)
        
if resp == "000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000":
    print("No response")
    os._exit(0)

