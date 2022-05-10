import select
# Test select.select() with POLLIN and POLLPRI events

import select, socket

msg = b'x' * 200000
MAX_COUNT = 10

def unpack_poll(poll, expected_flags):
    for fd, event in poll:
        assert event & ~select.POLLERR == expected_flags, 'bad event: %s' % event

sock, port = test_support.bind_port(socket.AF_INET, socket.SOCK_DGRAM)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(MAX_COUNT):
    s.sendto(msg, ('localhost', port))

r, w, x = select.select([sock], [], [], 20)
