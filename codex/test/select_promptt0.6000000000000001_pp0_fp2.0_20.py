import select
# Test select.select()

print('select.select()')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(0)
s.bind(('', 0))
s.listen(1)
print('port:', s.getsockname()[1])

while True:
    r, w, x = select.select([s], [], [], 5)
    if r:
        conn, addr = s.accept()
        print('Incoming connection from', addr)
