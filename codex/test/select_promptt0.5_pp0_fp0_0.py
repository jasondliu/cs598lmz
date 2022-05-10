import select
# Test select.select()

def accept(s, server_addr):
    client, addr = s.accept()
    print('Got connection from', addr)
    client.send(b'OHAI')
    client.close()

def read(s):
    text = s.recv(100)
    print('Read 100 bytes of text data:', text)

server_addr = '127.0.0.1', 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
s.bind(server_addr)
s.listen(1)

# Wait until a client connects
print('Listening at', s.getsockname())
client, addr = s.accept()
print('Accepted from', addr)
client.send(b'OHAI')
client.close()

# Wait until data arrives
