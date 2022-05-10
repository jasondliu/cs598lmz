import select
# Test select.select()

def accept(s, server_addr):
    conn, addr = s.accept()
    print('accept', conn, addr)
    conn.setblocking(False)
    data = conn.recv(1024)
    # A readable socket channel has data to recv
    print('echo', data)
    conn.send(b'Got it')
    conn.close()

def read(s):
    data = s.recv(1024)
    # A writable socket channel is ready to send data
    print('read', data)
    s.send(b'This is a message from client')
    s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# set socket recv buffer size, default is 4096
s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024)
s.bind(('localhost', 15000))
s.listen(10)
s.setblocking(False)

