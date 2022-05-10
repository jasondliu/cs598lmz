import select
# Test select.select

import select
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
s.listen(1)
s.setblocking(0)

print select.select([s], [], [], 0)
print select.select([s], [], [], 1)
print select.select([s], [], [], 2)
print select.select([s], [], [], 3)
print select.select([s], [], [], 4)
print select.select([s], [], [], 5)
print select.select([s], [], [], 6)
print select.select([s], [], [], 7)
print select.select([s], [], [], 8)
print select.select([s], [], [], 9)
print select.select([s], [], [], 10)
print select.select([s], [], [], 11)
print select.select([s], [], [], 12)
print select.select([s], [], [], 13)
print select
