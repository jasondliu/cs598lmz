import select
# Test select.select from the python stdlib.

socks = {}

def create_server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port)
    s.bind(server_address)
    s.listen(1)
    return s

def create_client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port)
    s.connect(server_address)
    return s

server = create_server(5678)
client = create_client(5678)

socks['server'] = server
socks['client'] = client

# server, client
for sock in select.select(socks.values(), socks.values(), [])[0]:
    data = sock.recv(1)
    print sock, data

server.close()
client.close()
