import select
# Test select.select blocks with a zero timeout
import socket, time
r, w, x = select.select([], [], [], 0.0)
print r
print w
print x
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 0))
s.listen(5)
r, w, x = select.select([s], [], [], 0.0)
print r
print w
print x
start = time.time()
r, w, x = select.select([], [], [], 0.0)
end = time.time()
print r
print w
print x
print end - start
start = time.time()
r, w, x = select.select([], [], [], 0.001)
end = time.time()
print r
print w
print x
print end - start
print ' ' * 35 + 'what time is it?'
start = time.time()
r, w, x = select.select([s], [], [], 0.0)
end = time.time()
print
