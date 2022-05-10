import select
# Test select.select()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 0))
# no blocking, timeout

rs, ws, xs = select.select([s], [], [], 0.0)
print(rs, ws, xs)


rs, ws, xs = select.select([s], [], [], 0.5)
print(rs, ws, xs)

print('send')
s.sendto('hi'.encode(), ('127.0.0.1', 8080))

rs, ws, xs = select.select([s], [], [], 0.5)
print(rs, ws, xs)

s.shutdown(socket.SHUT_RD)
rs, ws, xs = select.select([s], [], [], 0.5)
print(rs, ws, xs)

