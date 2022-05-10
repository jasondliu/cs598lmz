import socket
# Test socket.if_indextoname
#
#   $ gcc -shared -o test-if_indextoname.so test-if_indextoname.c
#   $ python -c 'import socket; import test-if_indextoname; \
#       test-if_indextoname.init(socket.if_indextoname)'

def init(if_indextoname):
    if_indextoname.argtypes = [ctypes.c_int]
    if_indextoname.restype = ctypes.c_char_p

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        name = if_indextoname(int(sys.argv[1]))
        print name
        #print [name]
