import select
# Test select.select()
s = socket.socket()
s.bind(('127.0.0.1', 0))
s.listen(1)
s.setblocking(0)

r, w, e = select.select([s], [], [], 0)
print(r)
print(w)
print(e)

s.close()
