import select
# Test select.select() on closed socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 0))
s.listen(2)
s.close()
try:
    select.select([s], [s], [s], 0)
except socket.error:
    pass
else:
    assert False
