import select
# Test select.select

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
SERVER_HOST = 'localhost'
SERVER_PORT = 8888
SERVER_ADDR = (SERVER_HOST, SERVER_PORT)
REQUEST_QUEUE_SIZE = 5

def handle_request(client_connection):
    request = client_connection.recv(1024)
    print(request.decode())
    http_response = b'HTTP/1.1 200 OK\r\n\r\nHello, World!'
    client_connection.sendall(http_response)

def server():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDR)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format
