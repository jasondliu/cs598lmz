import select
# Test select.select()

def accept(sock, mask):
	new_sock, addr = sock.accept()
	print('accepted, ', addr)
	sel.register(new_sock, select.EVENT_READ, read)

def read(conn, mask):
	data = conn.recv(1000)
	if data:
		print('echoing', repr(data), 'to', conn)
		conn.send(data)
	else:
		print('closing', conn)
		sel.unregister(conn)
		conn.close()

sock = socket.socket()
sock.bind(('localhost', 1234))
sock.listen(100)
sock.setblocking(False)

sel = select.epoll()
sel.register(sock, select.EVENT_READ, accept)

while True:
	events = sel.poll()
	for key, mask in events:
		callback = key.data
		callback(key.fileobj, mask)
