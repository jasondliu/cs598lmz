import socket
# Test socket.if_indextoname
# (https://github.com/numba/numba/issues/3936)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.bind((socket.gethostname(), 0))

ifname = socket.if_indextoname(s.getsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE))
print(ifname)

# Test socket.bind
# (https://github.com/dask/distributed/issues/4259)

def test_bind_with_ifname(nbytes):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((socket.gethostname(), 0, ifname))
    s.listen(1)
    s.accept()

test_bind_with_ifname.py_func = test_
