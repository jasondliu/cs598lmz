import select
# Test select.select() is implemented.
# The select module is optional and may be absent
# when this test is run.
try:
    for i in range(2):
        r, w, x = select.select([], [], [], 0.0)
except AttributeError:
    try:
        select.select
    except AttributeError:
        pass
    else:
        raise TestFailed("expected an AttributeError")
except TypeError:
    raise TestFailed("select.select() didn't accept 3 float params")

# Test the return values of select.select()
import socket
sv = socket.socket()
sv.bind(("", 0))
sv.listen(1)
s = socket.socket()
s.connect(sv.getsockname())
s.setblocking(0)
r, w, x = select.select([s], [s], [s])
assert r == [s], "Readability test failed on new connection"
assert w == [s], "Writeability test failed on new connection"
assert x == [s], "Exception test failed on new connection"

s
