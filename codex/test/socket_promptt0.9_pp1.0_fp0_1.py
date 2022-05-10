import socket
# Test socket.if_indextoname()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((b"", 0))  # pick arbitrary port number
s.connect(('127.0.0.1', 80))  # connect to some arbitrary address

ind = s.getsockname()[-1]
CPython = b"lo"
PyPy = b"lo0"
if os.name == "pypy":
    assert socket.if_indextoname(ind) == PyPy
else:
    assert socket.if_indextoname(ind) == CPython

with pytest.raises(socket.error) as ex:
    socket.if_indextoname(0)

if ex.value.args[0] == errno.EINVAL:
    skipmsg = "No suitable network device found"
elif ex.value.args[0] == errno.ENXIO:
    skipmsg = "No binding known yet"
elif ex.value.args[0] == errno.ENODEV:
    skipmsg
