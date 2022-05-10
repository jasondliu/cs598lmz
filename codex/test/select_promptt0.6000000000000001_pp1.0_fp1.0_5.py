import select
# Test select.select()

import socket

s = socket.socket()
s.bind(('', 1234))
s.listen(1)

s1, addr1 = s.accept()
s2, addr2 = s.accept()

