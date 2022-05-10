import select
# Test select.select()

import socket

s = socket.socket()
s.bind(('', 1234))
s.listen(1)

s1, addr1 = s.accept()
s2, addr2 = s.accept()

print select.select([s1], [], [], 0)
# ([<socket._socketobject object at 0x7f8a36b5c900>], [], [])
print select.select([s2], [], [], 0)
# ([], [], [])

print select.select([s1, s2], [], [], 0)
# ([<socket._socketobject object at 0x7f8a36b5c900>], [], [])

print select.select([s1, s2], [], [], 0.1)
# ([], [], [])

s1.send('hello')
print select.select([s1], [], [], 0)
# ([], [], [])

print select.select([s2], [], [], 0)
# ([<socket._socketobject object at 0x
