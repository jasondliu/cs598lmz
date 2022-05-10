import select
# Test select.select()

# Create a pair of connected sockets
if os.name == 'posix':
    # For Unix
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(s.getsockname())
    server_socket, addr = s.accept()
    s.close()
else:
    # For Windows
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 0))
    server_socket.listen(1)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_socket.getsockname())
    server_socket, addr = server_socket.accept()

print('Connection from', addr)

