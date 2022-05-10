import socket
socket.if_indextoname("23")

# ctypes_interface.h
def iplen():
        buf = c_buffer(OFP_MAX_PORT_NAME_LEN)
        lib.if_indextoname(23, buf)
        return buf.value

print("%s" % iplen())
