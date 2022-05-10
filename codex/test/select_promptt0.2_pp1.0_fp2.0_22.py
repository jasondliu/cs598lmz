import select
# Test select.select()

import socket

def test_select():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    s.listen(1)
    s.setblocking(0)
    port = s.getsockname()[1]
